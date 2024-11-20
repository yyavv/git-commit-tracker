class LetterData:
    def __init__(self, letter_data):
        """Initialize the grid with a list of lists representing rows and columns."""
        if not all(len(row) == len(letter_data[0]) for row in letter_data):
            raise ValueError("All rows in the letter data must have the same number of columns.")
        
        # Ensure letter_data is a list of strings
        if isinstance(letter_data[0], list):
            self.letter_data = [''.join(map(str, row)) for row in letter_data]
        else:
            self.letter_data = letter_data
    
    def to_flat_list(self):
        """Return a flattened list of 1s and 0s."""
        return [int(cell) for row in self.letter_data for cell in row]