"""
Simple Rock, Paper, Scissors game
"""

import random
import sys

# These variables keep track of the number of wins, losses and ties.
wins = 0
losses = 0
ties = 0

validMoves = {'r': 'rock', 'p': 'paper', 's': 'scissors'}

def get_input():
    """Prompts for and return player input"""
    while True: # The player input loop
        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
        player_input = input()
        if player_input == 'q':
            sys.exit() # Quit the program
        #if player_input == 'r' or player_input == 'p' or player_input == 's':
        if player_input in validMoves.keys():
            return player_input
        print('Type one of r, p, s, or q.')

def resolve_match():
    """Display and record the win/loss/tie."""
    global wins, losses, ties
    if playerMove == computerMove:
        print('It is a tie!')
        ties += 1
    elif (playerMove == 'r' and computerMove == 's') or \
            (playerMove == 'p' and computerMove == 'r') or \
            (playerMove == 's' and computerMove == 'p'):
        print('You win!')
        wins += 1
    elif (playerMove == 'r' and computerMove == 'p') or \
            (playerMove == 'p' and computerMove == 's') or \
            (playerMove == 's' and computerMove == 'r'):
        print('You lose!')
        losses += 1


print('ROCK, PAPER, SCISSORS')

while True: # The main game loop
    print(f'{wins} Wins, {losses} Losses, {ties} Ties')

    # Player choice
    playerMove = get_input()
    print(f'{validMoves[playerMove].upper()} versus...')

    # Computer choice
    computerMove = random.choice(list(validMoves.keys()))
    print(validMoves[computerMove].upper())

    # Evaluate moves and resolve match
    resolve_match()
