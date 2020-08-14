import unittest
from blackboxgame import BlackBoxGame


class MyTestCase(unittest.TestCase):
    def test_something(self):
        game = BlackBoxGame([(3, 2), (3, 7), (6, 4), (8, 7)])
        self.assertEqual(game.shoot_ray(5, 0), (9, 5))  # exit position should be (9, 5)
        self.assertEqual(game.get_score(), 23)
        game.print_board()
        game = BlackBoxGame([(2, 6), (7, 6), (7, 8)])
        self.assertEqual(game.shoot_ray(3, 9), (3, 9))
        self.assertEqual(game.get_score(), 24)
        game.print_board()
        game = BlackBoxGame([(3, 3), (2, 6), (7, 6)])
        self.assertEqual(game.shoot_ray(6, 0), None)
        self.assertEqual(game.get_score(), 24)
        game.print_board()


if __name__ == '__main__':
    unittest.main()
