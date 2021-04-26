from board import Board, InvalidMoveError


def get_move(board, player_x, player_o):
    if board.get_current_player() == "X":
        return player_x(board)
    else:
        return player_o(board)


def game(player_x, player_o):
    board = Board()

    while not board.is_game_over():
        v, h = get_move(board, player_x, player_o)
        try:
            board.make_move(v, h)
        except InvalidMoveError as error:
            print(error)
            continue
        print(board)

    print("Game over!")
    winner = board.get_winner()
    if winner is not None:
        print(f"The winner is {winner}")
    else:
        print("Draw")
