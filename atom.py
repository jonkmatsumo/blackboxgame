class Atom:
    """
    An Atom object has a position (represented by it's row and column values, respectively
    and an indicator to note if it has been discovered yet. The BlackBoardGame has a data structure
    containing every Atom for a particular instance of the BlackBoardGame and will communicate with
    the Atom via its methods to get its location and to get / change it's discovered indicator.
    """
    def __init__(self, row, col, discovered=False):
        """
        Creates an atom object
        :param row: an int, representing the atom's row (must be between 1 and 8)
        :param col: an int, representing the atom's column (must be between 1 and 8)
        :param discovered: a boolean, whether the atom has been discovered yet (False by default)
        """
        self._row = row
        self._col = col
        self._discovered = discovered

    def get_position(self):
        """
        Gets the position of the Atom
        :return: a tuple (row, col) containing the row and column of the atom
        """
        position = (self._row, self._col)
        return position

    def set_position(self, row, col):
        """
        Checks to make sure the given (row, col) is valid, then updates the Atom's position
        :param row: an int, representing the atom's row (must be between 1 and 8)
        :param col: an int, representing the atom's column (must be between 1 and 8)
        :return: a boolean indicating whether the position was successfully set or not
        """
        if not (1 <= row <= 8 and 1 <= col <= 8):
            # given position is invalid
            return False

        # otherwise, update position and return that operation was successful
        self._row = row
        self._col = col

        return True

    def is_discovered_yet(self):
        """
        Indicates whether the boolean has been discovered yet (initially False)
        :return: a boolean, whether the atom has been discovered yet
        """
        return self._discovered

    def discover(self):
        """
        Marks the Atom as discovered
        """
        self._discovered = True