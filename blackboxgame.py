from atom import Atom
from player import Player


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


class BlackBoxGame:
    """
    The BlackBoxGame class is the central class which organizes the game and
    interfaces with the children classes using composition (the BlackBoxGame
    has-a Player, has atom(s), has-a Board).
    """
    def __init__(self, atoms_list):
        """
        Sets up the game board and places the atoms in the board
        :param atoms_list: a list of tuples containing the positions of the atoms
        at the start of the game.
        """
        # make a set of all the atoms (for easier access)
        self._atoms = set([Atom(row, col) for row, col in atoms_list])

        # set up game board
        self._board = Board(10, 10)

        # set up user info
        self._player = Player(25)

        # set of entry and exit points of rays so far
        self._entry_and_exit_points = set()

    def shoot_ray(self, row, col):
        """
        shoots a ray starting from (row, col) that moves according to the following rules:
        1. a ray moves forward one step at a time in its direction until either:
            a. it encounters an exit point in its path
            b. it encounters an atom in its path - this is called a 'hit' and
            nothing (None) is returned
            c. it encounters the corner of an atom (but not the atom directly),
            in which case it rotates (if possible) or reverses direction.
        2. the ray charges the user 1 point for each entry/exit point. a hit or
            reflection costs the user 1 point while a detour costs the user 2 points
        :param row: the starting row of the ray
        :param col: the starting column of the ray
        :return: False if the starting position is not valid. The starting position must be
            in one of the edges of the grid (row or col must be 0 or 9 but not both)
            None if shoot_ray encounters a hit
            A tuple containing the exit position otherwise
        """
        # if (row, col) is not along the edges, not a valid entry point
        if (1 <= row <= 8 and 1 <= col <= 8) or (row, col) in [(0, 0), (0, 9), (9, 0), (9, 9)]:
            return False

        # if this exit/entry point has already been used, cannot shoot a ray.
        if (row, col) in self._entry_and_exit_points:
            return False
        # otherwise, add the entry point to the loop
        self._entry_and_exit_points.add((row, col))
        self._board.update_board(row, col, 's')

        direction = self._set_initial_direction(row, col)

        self._player.set_score(-1)
        current_position = (row, col)

        while True:
            # initial candidate move: move one step in current direction
            candidate_point = (current_position[0] + direction[0], current_position[1] + direction[1])

            # First, check to see if this would cause a reflection or hit. If so, return.
            if self._get_atom_at(candidate_point[0], candidate_point[1]) is not None:
                # check for reflection
                if current_position[0] == row and current_position[1] == col:
                    # mark position as an exit position and return the current position
                    self._board.update_board(current_position[0], current_position[1], 'e')
                    return current_position
                # otherwise, this is a hit. return None
                return None

            # Second, check if there are any bordering Atoms (that would cause a detour or reflection)
            direction = self._check_if_atom_borders(current_position, direction)

            # Direction has been adjusted / verified, take step
            current_position = (current_position[0] + direction[0], current_position[1] + direction[1])

            # See if taking new step puts the ray in an exit position
            if current_position[0] in [0, 9] or current_position[1] in [0, 9]:
                if current_position[0] != row or current_position[1] != col:
                    # miss or detour => new exit point, deduct one more point
                    self._player.set_score(-1)
                    self._entry_and_exit_points.add((current_position[0], current_position[1]))
                self._board.update_board(current_position[0], current_position[1], 'e')
                return current_position

    def guess_atom(self, row, col):
        """
        checks the given location (row, col) and adjusts score accordingly
        :param row: int - the row of the user's guess
        :param col: int - the column of the user's guess
        :return: bool - True if an atom is at that location, otherwise False
        """
        # if already guessed, return if there's anything at that spot (no modifying score)
        can_guess = self._player.guess(row, col)

        # initially, assume False (change to True if there is an atom at this position)
        guess_correct = False

        # search through set of atoms for a match
        atom = self._get_atom_at(row, col)
        if atom is not None:
            # if an atom was found at this position, indicate the guess is correct
            guess_correct = True
            # if this is a valid guess, update atom to be discovered and update board
            if can_guess and atom.is_discovered_yet() is False:
                atom.discover()
                self._board.update_board(row, col, 'o')

        if can_guess and guess_correct is False:
            self._board.update_board(row, col, 'x')
            self._player.set_score(-5)

        return guess_correct

    def get_score(self):
        """
        :return: an integer, the Player's score
        """
        return self._player.get_score()

    def atoms_left(self):
        """
        :return: an integer, the number of undiscovered atoms remaining
        """
        count = 0
        for atom in self._atoms:
            if atom.is_discovered_yet() is False:
                count += 1
        return count

    def _get_atom_at(self, row, col):
        """
        Helper method, used to get the Atom at a given position (row, col)
        :param row: the row of the target Atom (must be between 1 and 8, inclusive)
        :param col: the column of the target atom (must be between 1 and 8, inclusive)
        :return: an Atom object whose position matches (row, col), or None if none exist
        """
        for atom in self._atoms:
            # if the position of the atom matches the position of guess, match is found
            atom_position = atom.get_position()
            if atom.get_position() == (row, col):
                return atom

        # no match found, return None
        return None

    def _set_direction(self, direction):
        """
        Helper Method, Returns a coordinate pair that indicates what one step in that direction is
        :param direction: A string, one of the following:
        -   'down' - move one down along current column, represented as (1, 0)
        -   'left' - move one left along current row, represented as (0, -1)
        -   'right' - move one right along current row, represented as (0, 1)
        -   'up' - move one up along current column, represented as (-1, 0)
        :return: a tuple containing the row and col of move in given direction
        """
        directions = {"down": (1, 0), "left": (0, -1), "right": (0, 1), "up": (-1, 0)}
        return directions[direction]

    def _set_initial_direction(self, row, col):
        """
        Helper Method, Determines which way to set the direction based on the starting position
        (to determine what conditions to use for _set_direction). These are determined by the
        following using the notation (row, col):
        -   'down' - move one down along current column, starting position is (0, x)
        -   'left' - move one left along current row, represented as (9, x)
        -   'right' - move one right along current row, represented as (x, 0)
        -   'up' - move one up along current column, represented as (x, 9)
        :param row: the row of the starting position
        :param col: the column of the starting position
        :return: a tuple containing the row and col of move in given direction
        """
        if row == 0:
            direction = self._set_direction('down')
        elif row == 9:
            direction = self._set_direction('up')
        elif col == 0:
            direction = self._set_direction('right')
        else:
            direction = self._set_direction('left')
        return direction

    def _check_if_atom_borders(self, candidate_point, direction):
        """
        Checks if a point borders any atoms and changes its direction if so
        :param candidate_point: a tuple containing the row and column of the candidate points
        :param direction: a tuple indicating the direction the ray is traveling
        (in case of rotation or reflection, changes this direction) as follows:
        -   (1, 0) - move one down along current column, represented
        -  (0, -1) - move one left along current row
        -   (0, 1) - move one right along current row
        -  (-1, 0) - move one up along current column
        :return: a tuple representing the direction after any detours, rotations.
                 can be unchanged in the case that there are no neighboring atoms.
        """
        # Case 1: Down
        if direction == (1, 0):
            direction = self._check_if_atom_borders_down(candidate_point)

        # Case 2: Left
        elif direction == (0, -1):
            direction = self._check_if_atom_borders_left(candidate_point)

        # Case 3: Right
        elif direction == (0, 1):
            direction = self._check_if_atom_borders_right(candidate_point)

        # Case 4: Up
        elif direction == (-1, 0):
            direction = self._check_if_atom_borders_up(candidate_point)

        return direction

    def _check_if_atom_borders_down(self, candidate_point):
        """
        Helper method for _check_if_atom_borders, handles case direction is down.
        :param candidate_point: a tuple containing the row and column of the candidate point
        in the form (row, col)
        :return: a tuple indicating the direction of the next step
        """
        row, col = candidate_point

        # check if it touches an atom to its left or right
        bordering_left = self._get_atom_at(row + 1, col - 1)
        bordering_right = self._get_atom_at(row + 1, col + 1)

        # if both, this is a reflection
        if bordering_left is not None and bordering_right is not None:
            direction = self._set_direction("up")

        # if just to its left, rotate right
        elif bordering_left is not None:
            direction = self._set_direction("right")

        # if just to its right, rotate left
        elif bordering_right is not None:
            direction = self._set_direction("left")

        # otherwise, keep direction down
        else:
            direction = self._set_direction("down")

        return direction

    def _check_if_atom_borders_left(self, candidate_point):
        """
        Helper method for _check_if_atom_borders, handles case direction is left
        :param candidate_point: a tuple containing the row and column of the candidate point
        in the form (row, col)
        :return: a tuple indicating the direction of the next step
        """
        row, col = candidate_point

        # check if it touches an atom above or below
        bordering_above = self._get_atom_at(row - 1, col - 1)
        bordering_below = self._get_atom_at(row + 1, col - 1)

        # if both, this is a reflection
        if bordering_above is not None and bordering_below is not None:
            direction = self._set_direction("right")

        # if just above, rotate downward
        elif bordering_above is not None:
            direction = self._set_direction("down")

        # if just below, rotate upward
        elif bordering_below is not None:
            direction = self._set_direction("up")

        # otherwise, keep direction left
        else:
            direction = self._set_direction("left")

        return direction

    def _check_if_atom_borders_right(self, candidate_point):
        """
        Helper method for _check_if_atom_borders, handles case direction is right
        :param candidate_point: a tuple containing the row and column of the candidate point
        in the form (row, col)
        :return: a tuple indicating the direction of the next step
        """
        row, col = candidate_point

        # check if it touches an atom above or below
        bordering_above = self._get_atom_at(row - 1, col + 1)
        bordering_below = self._get_atom_at(row + 1, col + 1)

        # if both, this is a reflection
        if bordering_above is not None and bordering_below is not None:
            direction = self._set_direction("left")

        # if just above, rotate downward
        elif bordering_above is not None:
            direction = self._set_direction("down")

        # if just below, rotate upward
        elif bordering_below is not None:
            direction = self._set_direction("up")

        # otherwise, keep direction right
        else:
            direction = self._set_direction("right")

        return direction

    def _check_if_atom_borders_up(self, candidate_point):
        """
        Helper method for _check_if_atom_borders, handles case direction is up
        :param candidate_point: a tuple containing the row and column of the candidate point
        in the form (row, col)
        :return: a tuple indicating the direction of the next step
        """
        row, col = candidate_point

        # check if it touches an atom to its left or right
        bordering_left = self._get_atom_at(row - 1, col - 1)
        bordering_right = self._get_atom_at(row - 1, col + 1)

        # if both, this is a reflection
        if bordering_left is not None and bordering_right is not None:
            direction = self._set_direction("down")

        # if just to its left, rotate right
        elif bordering_left is not None:
            direction = self._set_direction("right")

        # if just to its right, rotate left
        elif bordering_right is not None:
            direction = self._set_direction("left")

        # otherwise, keep direction up
        else:
            direction = self._set_direction("up")

        return direction

    def print_board(self):
        """
        Prints out the board
        """
        self._board.print_board()
