from game import game
from player import get_human_move, get_computer_move

print("Welcome to the Tic Tac Toe game!")

while True:
    print("Let's play!")
    game(get_human_move, get_computer_move)
