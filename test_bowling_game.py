from unittest import TestCase
from bowling_game import Game


class TestBowlingGame(TestCase):
    def setUp(self):
        self.game = Game()

    def test_gutter_game(self):
        self.roll_all(20 * [0])

        self.assertEqual(0, self.game.score())

    def test_all_ones(self):
        self.roll_all(20 * [1])

        self.assertEqual(20, self.game.score())

    def test_one_spare_bonus(self):
        self.roll_all([5, 5, 3] + 17 * [0])

        self.assertEqual(16, self.game.score())

    def test_one_strike_bonus(self):
        self.roll_all([10, 3, 4] + 16 * [0])

        self.assertEqual(24, self.game.score())

    def test_perfect_game(self):
        self.roll_all(12 * [10])

        self.assertEqual(300, self.game.score())

    def roll_all(self, rolls):
        for pins in rolls:
            self.game.roll(pins)
