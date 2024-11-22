from .letter_data import LetterData
from .letters import LETTERS_GRID  # Assuming this is where LETTERS_GRID is defined.
import time
import os
import sys
import platform

class Message:
    def __init__(self, message):
        """Initialize the Message with a string and create LetterData objects."""
        self.message = message.upper()
        self.letters = self.create_letter_data(message)
        self.x_count = self.calculate_x_count()
        self._first_animation = True  # Flag to track first animation

    def clear_console(self):
        """
        Cross-platform method to clear the console.
        Works on Windows, macOS, Linux, and other Unix-like systems.
        """
        system = platform.system().lower()
        
        if system == 'windows':
            # For Windows
            _ = os.system('cls')
        else:
            # For Unix, Linux, macOS
            _ = os.system('clear')

    def create_letter_data(self, message):
        """Create a list of LetterData objects for each letter in the message."""
        letter_data_list = []
        for char in message.upper():
            if char != ' ':
                if char in LETTERS_GRID: 
                    letter_data = LetterData(LETTERS_GRID[char])
                    letter_data_list.append(letter_data)
            else:
                letter_data_list.append(None)
        return letter_data_list

    def calculate_x_count(self):
        """Calculate total number of 1s in the message."""
        total = 0
        for letter in self.letters:
            if letter:
                total += sum(row.count('1') for row in letter.letter_data)
        return total

    def get_letter_x_counts(self):
        """Return a dictionary of X counts for each letter in the message."""
        counts = {}
        for i, letter in enumerate(self.letters):
            if letter:
                char = self.message.upper()[i]
                counts[char] = sum(row.count('1') for row in letter.letter_data)
        return counts

    def animate_message_by_row(self, delay=0.05, show_progress=False):
        """Animate the message row by row with smooth scrolling."""
        # Clear console only on first animation
        if self._first_animation:
            self.clear_console()
            self._first_animation = False

        total_rows = 5
        current_display = [''] * total_rows
        x_printed = 0
        
        # Build complete rows
        complete_rows = [''] * total_rows
        for letter_data in self.letters:
            if letter_data:
                for i in range(total_rows):
                    converted_row = letter_data.letter_data[i].replace('1', 'X').replace('0', ' ')
                    complete_rows[i] += converted_row + "  "
            else:
                for i in range(total_rows):
                    complete_rows[i] += "     "

        # Print initial empty lines
        print('\n' * 2)
        
        # Move cursor up to start position
        sys.stdout.write(f"\033[{total_rows + (2 if show_progress else 0)}A")
        sys.stdout.flush()

        # Animate row by row
        for row_idx in range(total_rows):
            current_display[row_idx] = ''
            for char_idx in range(len(complete_rows[row_idx])):
                char = complete_rows[row_idx][char_idx]
                current_display[row_idx] += char
                
                if char == 'X':
                    x_printed += 1
                    # Move cursor to start of the display area
                    sys.stdout.write(f"\033[{total_rows + (2 if show_progress else 0)}A")
                    
                    # Print current state
                    for i in range(total_rows):
                        if i < row_idx + 1:
                            print(current_display[i])
                        else:
                            print()
                            
                    if show_progress:
                        print(f"\nProgress: {x_printed}/{self.x_count} X's printed")
                    
                    sys.stdout.flush()
                    time.sleep(delay)

        # Final newline for clean finish
        print()

    def print_stats(self):
        """Print statistics about the message."""
        print(f"\nMessage Statistics:")
        print(f"Total X count: {self.x_count}")
        print("\nX count per letter:")
        letter_counts = self.get_letter_x_counts()
        for char, count in letter_counts.items():
            print(f"  {char}: {count}")

    def __str__(self):
        """Return the string representation of the entire message."""
        rows = ['' for _ in range(5)]
        for letter_data in self.letters:
            if letter_data:
                for i in range(5):
                    converted_row = letter_data.letter_data[i].replace('1', 'X').replace('0', 'O')
                    rows[i] += converted_row + "  "
            else:
                for i in range(5):
                    rows[i] += "     "
        return "\n".join(rows)