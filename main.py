# Author: Jonathan Matsumoto
# Date: 8/3/2020
# Description: Implementation of Black Box (see https://en.wikipedia.org/wiki/Black_Box_(game)


class BlackBoxGame:
    """ sets up and maintains a game of Black Box """
    def __init__(self, atoms):
        """ sets up the game board and places the atoms in the board """
        # make a set of all the atoms (for easier access)
        self._atoms = set([atom for atom in atoms])

        # set up game board as a 10 x 10 grid
        self._board = [['' for _ in range(10)] for _ in range(10)]

        # place atoms in the board:
        for atom in self._atoms:
            row, col = atom
            self._board[row][col] = 'u'  # 'u' is undiscovered, 'd' is discovered

        # set up user info
        self._score = 25
        self._guesses = set()

    def shoot_ray(self, row, col):
        """ TO-DO: shoots a ray and returns the result."""
        pass

    def guess_atom(self, row, col):
        """
        checks the given location (row, col) and adjusts score accordingly
        :param row: int - the row of the user's guess
        :param col: int - the column of the user's guess
        :return: bool - True if an atom is at that location, otherwise False
        """
        # if already guessed, return if there's anything at that spot (no modifying score)
        if (row, col) in self._guesses:
            return self._board[row][col] != ''

        # otherwise, add this pair to the guesses
        self._guesses.add((row, col))

        # found an atom, mark it as discovered and return True
        if self._board[row][col] != '':
            self._board[row][col] = 'd'
            return True

        # incorrect guess, lower score and return False
        self._score -= 5
        return False

    def get_score(self):
        """ returns the current score """
        return self._score

    def atoms_left(self):
        """ returns the number of undiscovered atoms remaining """
        count = 0
        for atom in self._atoms:
            row, col = atom
            if self._board[row][col] == 'u':
                count += 1
        return count

    def print_board(self):
        """ helper method: prints out the game board """
        cur_row = ""
        for i in range(len(self._board)):
            for j in range(len(self._board[0])):
                # add '-' if nothing at (i, j), otherwise display its contents
                if self._board[i][j] == '':
                    cur_row += '-'
                else:
                    cur_row += self._board[i][j]
            # after processing row, print and reset it
            print(cur_row)
            cur_row = ""
