class Player:
    """
    The Player class contains all the information specific to a player of the
    BlackBoxGame. Namely, their score (initially 25, but decreases as they are
    charged for various moves) and a set of their past guesses. The BlackBoxGame
    class interfaces directly with the Player class to get their score and to
    add new guesses (since a player shouldn't be charged for the same guess twice).
    """
    def __init__(self, starting_score = 25):
        """
        Creates a Player object with a starting score and no guesses yet.
        :param starting_score: the player's starting score (initially 25)
        """
        self._score = starting_score
        self._guesses = set()

    def get_score(self):
        """
        Gets the player's current score
        :return: an integer, the player's current score
        """
        return self._score

    def set_score(self, score_change):
        """
        Changes the player's score by score_change
        :param score_change: an int, the amount to change player's score by
        """
        self._score += score_change

    def get_guesses(self):
        """
        Get's all of the player's past guesses
        :return: a set containing the player's previous guesses
        """
        return self._guesses

    def guess(self, row, col):
        """
        checks if the player has guessed that position already. if so, player cannot guess that position.
        if not, updates the list of player guesses and indicates player can make guess successfully
        :param row: the row of the player's guess
        :param col: the column of the player's guess
        :return: False if guess was previously made, True if player was able to guess that position
        """
        if (row, col) in self._guesses:
            # player has already guessed this position
            return False

        # player has not guessed this position already, now makes this guess
        self._guesses.add((row, col))
        return True