from assets.message import Message
from datetime import datetime, timedelta
from typing import List, Optional

class CommitTracker:
    def __init__(self, message_instance):
        """
        Initialize CommitTracker with a Message instance.
        """
        self._message_instance = message_instance
        self.today = datetime.now()
        self.date = self.today.strftime("%d-%m-%Y")
        self.day = self.today.strftime("%A")
        self.start_date = self.today # Save the start date for later use
        self.end_date = None

    def calculateNextMonday(self, weekday: int) -> timedelta:
        """Calculate days until next Monday."""
        return timedelta(days=7 - weekday % 7)

    def calculateDays(self) -> List[List[Optional[str]]]:
        """Calculate commit dates for the message pattern."""
        print("Calculating days for commit tracker")
        
        # Start from next Monday
        self.today += self.calculateNextMonday(self.today.weekday())
        
        # Get the letter grids and iterate over the message
        result_dates = []
        
        # Iterate through actual message characters and their corresponding LetterData
        for idx, letter_data in enumerate(self._message_instance.letters):
            if letter_data:
                grid = letter_data.letter_data  # This is already a list of strings
                letter_dates = []
                
                # Process each column in the grid, top to bottom
                for col in range(5):  # Assuming 5x5 grid
                    
                    for row in range(5):
                        current_cell = grid[row][col]
                        if current_cell == '1':
                            letter_dates.append(self.today.strftime("%d-%m-%Y"))
                        else:
                            letter_dates.append(None)
                        self.today += timedelta(days=1)  # Add 1 day for each cell in the grid
                    
                    self.today += self.calculateNextMonday(self.today.weekday())  # Add days until next Monday

                result_dates.append(letter_dates)
                self.today += timedelta(days=7)  # Add 7 days for spacing between letters
            else:
                # Handle spaces
                result_dates.append([None] * 25)
                self.today += timedelta(days=7)  # Add extra 7 days for new word spacing
        
        self.end_date = result_dates[-1][-1]  # Save the end date for later use
        self.print_result(result_dates)
        return result_dates

    def print_result(self, result_dates: List[List[Optional[str]]]):
        """Print commit dates for each letter."""
        print("\nCommit Dates:")
        
        # Iterate through the actual message characters
        for idx, dates in enumerate(result_dates):
            if dates is None or len(dates) == 0:
                continue
            
            # Get the actual letter from the message
            current_letter = self._message_instance.message[idx]
            print(f"Letter {current_letter}:")
            
            # Print dates in a 5x5 grid format
            for row in range(5):
                row_dates = []
                for col in range(5):
                    index = col * 5 + row  # Calculate correct index for column-first order
                    date = dates[index] if index < len(dates) else None
                    row_dates.append(date if date else "---")
                print(" | ".join(row_dates))
            print("-" * 75)

    def print_commit_summary(self):
        """Print a summary of total commits needed."""
        total_commits = sum(
            sum(1 for row in letter.letter_data for cell in row if cell == '1')
            for letter in self._message_instance.letters
            if letter is not None
        )
        print(f"\nTotal commits needed: {total_commits}")
        print(f"Starting from: {self.date} ({self.day})")
        
        # Ensure self.end_date is a datetime object
        if isinstance(self.end_date, str):
            self.end_date = datetime.strptime(self.end_date, "%d-%m-%Y")
        
        print(f"Ending on: {self.end_date.strftime('%d-%m-%Y')} ({self.end_date.strftime('%A')})")
        
        # Calculate total days
        total_days = (self.end_date - self.start_date).days
        print(f"Total days: {total_days}")

# today = datetime.datetime.now() 

# date = today.strftime("%d-%m-%Y")

# day = today.strftime("%A")

