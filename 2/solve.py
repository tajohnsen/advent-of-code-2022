from itertools import *

# quality of life
A = "A"
B = "B"
C = "C"
X = "X"
Y = "Y"
Z = "Z"

# (1 for Rock, 2 for Paper, and 3 for Scissors)
ROCK = 1
PAPER = 2
SCISSORS = 3

# (0 if you lost, 3 if the round was a draw, and 6 if you won)
LOSE = 0
DRAW = 3
WIN = 6

score1_table = dict(
    A=dict(
        X=ROCK + DRAW,
        Y=PAPER + WIN,
        Z=SCISSORS + LOSE
    ),
    B=dict(
        X=ROCK + LOSE,
        Y=PAPER + DRAW,
        Z=SCISSORS + WIN
    ),
    C=dict(
        X=ROCK + WIN,
        Y=PAPER + LOSE,
        Z=SCISSORS + DRAW
    )
)


'''
X means you need to lose, 
Y means you need to end the round in a draw, and 
Z means you need to win.
'''
score2_table = dict(
    A=dict(
        X=LOSE + SCISSORS,
        Y=DRAW + ROCK,
        Z=WIN + PAPER
    ),
    B=dict(
        X=LOSE + ROCK,
        Y=DRAW + PAPER,
        Z=WIN + SCISSORS
    ),
    C=dict(
        X=LOSE + PAPER,
        Y=DRAW + SCISSORS,
        Z=WIN + ROCK
    )
)


def score1(them: str, us: str) -> int:
    return score1_table[them][us]


def score2(them: str, us: str) -> int:
    return score2_table[them][us]


def main():
    with open('input', 'r') as in_file:
        data = in_file.readlines()

    print(list(accumulate(starmap(score1, (choice.split(' ') for choice in map(lambda x: x.strip(), iter(data))))))[-1])
    print(list(accumulate(starmap(score2, (choice.split(' ') for choice in map(lambda x: x.strip(), iter(data))))))[-1])


if __name__ == '__main__':
    main()
