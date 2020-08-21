class Board:
    """
    The Board class represents the game Board. It is initially initialized using a list
    comprehension and adjusted to exclude the corners. The BlackBoxGame updates the Board
    when the user shoots a ray or guesses a value. The characters on the board are:
        -   '-' - an uninitialized space (if row or col is 0 or 9, entry point for ray,
            otherwise a spot the user can guess)
        -   'x' - indicates the position of an incorrect guess
        -   'o' - indicates the position of a discovered Atom
        -   's' - indicates the entry position of a ray
        -   'e' - indicates the exit position of a ray
    """
    def __init__(self, row, col):
        """
        Creates a Board of row x col dimensions
        :param row: an int, the number of rows in the Board
        :param col: an int, the number of columns in the Board
        """
        self._board = [['-' for _ in range(row)] for _ in range(col)]
        # mark corners as empty
        for row, col in [(0, 0), (0, 9), (9, 0), (9, 9)]:
            self._board[row][col] = ' '

    def update_board(self, row, col, char):
        """
        Updates board at position (row, col) to contain the given character
        :param row: an int, the row in the Board to update
        :param col: an int, the column in the Board to update
        :param char: a string, the value to place in (row, col).
        The recommended inputs are:
        -   'x' - indicates the position of an incorrect guess
        -   'o' - indicates the position of a discovered Atom
        -   's' - indicates the entry position of a ray
        -   'e' - indicates the exit position of a ray
        """
        self._board[row][col] = char

    def print_board(self):
        """
        Prints out current game board
        """
        current_row = ''
        for row in range(len(self._board)):
            for col in range(len(self._board[0])):
                current_row += self._board[row][col]
            print(current_row)
            current_row = ''