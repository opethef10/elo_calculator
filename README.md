# Elo Rating Calculation Script

This script calculates the Elo rating adjustment for two players based on their current ratings and the outcome of their match. The Elo rating system, created by Arpad Elo, is widely used in competitive games and sports to rank players.

## Features

- Calculate the Elo rating adjustment for two players.
- Specify the outcome of the match (win, loss, draw).
- Adjustable K-factor to influence rating sensitivity.

## Usage

To run the script, use the following command in your terminal:

```bash
python elo_calculator.py <rating1> <rating2> [<score>] [<k>]
```

## Arguments

- `rating1`: The current rating of the first player (integer).
- `rating2`: The current rating of the second player (integer).
- `score`: The score for the first player (0: loss, 0.5: draw, 1: win). Default is 1 (win).
- `k`: The K-factor for the rating adjustment, affecting the sensitivity of rating changes. Default is 40.

## Example

To calculate the Elo rating adjustment for two players with ratings of 1200 and 1300, where the first player wins, use:

```bash
python elo_calculator.py 1200 1300 1 40
```

## Requirements

- Python 3.x

