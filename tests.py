import unittest
from elo_calculator import elo  # Adjust the import based on your file structure

class TestEloFunction(unittest.TestCase):

    def test_elo_win(self):
        # Test case where player 1 wins
        rating1 = 1200
        rating2 = 1300
        score = 1  # Player 1 wins
        k = 40
        expected_gain = 26  # Expected gain for player 1
        self.assertEqual(elo(rating1, rating2, score, k), expected_gain)

    def test_elo_loss(self):
        # Test case where player 1 loses
        rating1 = 1200
        rating2 = 1300
        score = 0  # Player 1 loses
        k = 40
        expected_gain = -14  # Expected loss for player 1
        self.assertEqual(elo(rating1, rating2, score, k), expected_gain)

    def test_elo_draw(self):
        # Test case where players draw
        rating1 = 1200
        rating2 = 1300
        score = 0.5  # Draw
        k = 40
        expected_gain = 6  # No gain for player 1 in a draw
        self.assertEqual(elo(rating1, rating2, score, k), expected_gain)

    def test_elo_with_different_k(self):
        # Test case with a different K-factor
        rating1 = 1200
        rating2 = 1300
        score = 1  # Player 1 wins
        k = 20  # Different K-factor
        expected_gain = 13  # Expected gain for player 1 with K=20
        self.assertEqual(elo(rating1, rating2, score, k), expected_gain)

    def test_elo_boundary_conditions(self):
        # Test boundary conditions
        rating1 = 1500
        rating2 = 1500
        score = 1  # Player 1 wins
        k = 40
        expected_gain = 20  # No change since both players are equally rated
        self.assertEqual(elo(rating1, rating2, score, k), expected_gain)

if __name__ == '__main__':
    unittest.main()

