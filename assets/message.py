from .letter_data import LetterData
from .letters import LETTERS_GRID  # Assuming this is where LETTERS_GRID is defined.

class Message:
    def __init__(self, message):
        """Initialize the Message with a string and create LetterData objects."""
        self.message = message
        self.letters = self.create_letter_data(message)

    def create_letter_data(self, message):
        """Create a list of LetterData objects for each letter in the message."""
        letter_data_list = []
        for char in message.upper():  # Convert the message to uppercase
            if char != ' ':
                if char in LETTERS_GRID:  # If it's a valid letter
                    letter_data = LetterData(LETTERS_GRID[char])
                    letter_data_list.append(letter_data)
            else:
                # If it's a space, add a placeholder (None or some other representation)
                letter_data_list.append(None)
        return letter_data_list

    def __str__(self):
        """Return the string representation of the entire message, printing all rows side by side."""
        rows = ['' for _ in range(5)]  # Prepare a list for the 5 rows

        for letter_data in self.letters:
            if letter_data:
                for i in range(5):  # There are 5 rows in each letter grid
                    # Convert 1s to 'X' and 0s to 'O'
                    # converted_row = letter_data.letter_data[i].replace('1', '■').replace('0', '□')
                    # converted_row = letter_data.letter_data[i].replace('1', 'X').replace('0', ' ')
                    converted_row = letter_data.letter_data[i].replace('1', '⬛').replace('0', '⬜')
                    rows[i] += converted_row + "  "  # Add space between letters
            else:
                for i in range(5):  # Add space between words
                    rows[i] += "     "  # Adjust the spacing between words

        # Join all rows with a newline and return the final formatted message
        result = "\n".join(rows)
        return  "\n" + result