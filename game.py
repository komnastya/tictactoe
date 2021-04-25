import random
from board import Board, InvalidMoveError


def get_computer_move(board):
    while True:
        v = random.randint(0, 2)
        h = random.randint(0, 2)
        if board.is_cell_empty(v, h):
            print(f"\nComputer move is: {v + 1} {h + 1}")
            return v, h


def get_human_move(board):
    while True:
        move = input(f"\nHuman move is: ")
        parts = move.strip().split(" ")
        if len(parts) == 2:
            try:
                v, h = parts
                v, h = int(v), int(h)
                if 1 <= v <= 3 and 1 <= h <= 3:
                    return (v - 1, h - 1)
            except ValueError:
                pass
        print("Please enter two numbers in range [1,3]")


def get_move(board):
    if board.get_current_player() == "X":
        return get_human_move(board)
    else:
        return get_computer_move(board)


def game():
    board = Board()

    while not board.is_game_over():
        v, h = get_move(board)
        try:
            board.make_move(v, h)
        except InvalidMoveError as error:
            print(error)
            continue
        print (board)

    print("Game over!")
    winner = board.get_winner()
    if winner is not None:
        print(f"The winner is {winner}")
    else:
        print("Draw")
