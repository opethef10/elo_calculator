#! /usr/bin/env python
"""
Elo Rating Calculation Script

This script calculates the Elo rating adjustment for two players based on their
current ratings and the outcome of their match. The Elo rating system is used
in various competitive games and sports to rank players.
"""

import argparse

M = 400  # Constant used in Elo calculation
DEFAULT_K = 40  # Default K-factor


def elo(rating1, rating2, score=1, K=DEFAULT_K):  
    """
    Calculate the Elo rating adjustment.

    Args:
        rating1 (int): The rating of the first player.
        rating2 (int): The rating of the second player.
        score (float): The score of the first player (0: loss, 0.5: draw, 1: win).
        K (int): The K-factor for the rating adjustment.

    Returns:
        int: The rating change for the first player.
    """
    delta = rating2 - rating1
    expected = 1 / (1 + 10 ** (delta / M))
    return round(K * (score - expected))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('rating1', type=int, help='Rating of the first player (e.g., 1200)')
    parser.add_argument('rating2', type=int, help='Rating of the second player (e.g., 1300)')
    parser.add_argument('score', type=float, nargs='?', default=1,
                        help='Score for the first player (0: loss, 0.5: draw, 1: win; default: 1)')
    parser.add_argument('k', type=int, nargs='?', default=DEFAULT_K,
                        help='K-factor for the rating adjustment (default: 40)')

    args = parser.parse_args()

    # Validate score is between 0 and 1
    if not (0 <= args.score <= 1):
        raise SystemExit("Error: Score must be a float between 0 and 1, inclusive.")

    gain = elo(args.rating1, args.rating2, args.score, args.k)
    new_rating1 = args.rating1 + gain
    new_rating2 = args.rating2 - gain

    print(f"Initial ratings: {args.rating1}, {args.rating2}")
    print(f"Gain: {gain}")
    print(f"New ratings: {new_rating1}, {new_rating2}")

