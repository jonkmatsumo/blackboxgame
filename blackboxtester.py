import unittest
from blackboxgame import BlackBoxGame


class MyTestCase(unittest.TestCase):
    def test_something(self):
        game = BlackBoxGame([(3, 2), (3, 7), (6, 4), (8, 7)])
        self.assertEqual(game.shoot_ray(5, 0), (9, 5))  # exit position should be (9, 5)
        self.assertEqual(game.get_score(), 23)
        game = BlackBoxGame([(2, 6), (7, 6), (7, 8)])
        self.assertEqual(game.shoot_ray(3, 9), (3, 9))
        self.assertEqual(game.get_score(), 24)
        game = BlackBoxGame([(3, 3), (2, 6), (7, 6)])
        self.assertEqual(game.shoot_ray(6, 0), None)
        self.assertEqual(game.get_score(), 24)

    def test_hit(self):
        game = BlackBoxGame([(3, 2), (3, 7), (6, 4), (8, 7)])
        self.assertEqual(game.shoot_ray(6, 9), None)

    def test_deflection(self):
        game = BlackBoxGame([(3, 2), (3, 7), (6, 4), (8, 7)])
        self.assertEqual(game.shoot_ray(5, 9), (0, 5))

    def test_double_deflection(self):
        game = BlackBoxGame([(6, 4), (6, 6)])
        self.assertEqual(game.shoot_ray(0, 5), (0, 5))

    def test_reflection(self):
        game = BlackBoxGame([(3, 2), (3, 7), (6, 4), (8, 7)])
        self.assertEqual(game.shoot_ray(9, 7), (9, 7))

    def test_miss(self):
        game = BlackBoxGame([(3, 2), (3, 7), (6, 4), (8, 7)])
        self.assertEqual(game.shoot_ray(1, 9), (1, 0))

    def test_detour(self):
        game = BlackBoxGame([(3, 2), (3, 7), (6, 4), (8, 7)])
        self.assertEqual(game.shoot_ray(0, 3), (0, 6))
        self.assertEqual(game.shoot_ray(4, 9), (7, 9))

    def test_multiple_deflections(self):
        game = BlackBoxGame([(3, 2), (3, 7), (6, 4), (8, 7)])
        self.assertEqual(game.shoot_ray(5, 0), (9, 5))

    def test_multiple_deflections_reflection(self):
        game = BlackBoxGame([(2, 6), (7, 6), (7, 8)])
        self.assertEqual(game.shoot_ray(3, 9), (3, 9))

    def test_multiple_deflections_hit(self):
        # TO-DO: None != (4,9)
        game = BlackBoxGame([(2, 6), (3, 4), (7, 6)])
        self.assertEqual(game.shoot_ray(6, 0), None)


if __name__ == '__main__':
    unittest.main()
