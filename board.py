class InvalidMoveError(Exception):
    pass


class Board:
    def __init__(self):
        self._board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self._moves = []
        self._winner = None

    def make_move(self, v, h):
        if self.is_game_over():
            raise InvalidMoveError("Game is already over.")
        if not self.is_cell_empty(v, h):
            raise InvalidMoveError(f"Cell ({v+1}, {h+1}) is already occupied.")
        player = self.get_current_player()
        self._moves.append((v, h))
        board = self._board
        board[v][h] = player
        if (
            board[v][0] == board[v][1] == board[v][2] != " "
            or board[0][h] == board[1][h] == board[2][h] != " "
            or board[0][0] == board[1][1] == board[2][2] != " "
            or board[2][0] == board[1][1] == board[0][2] != " "
        ):
            self._winner = player

    def is_game_over(self):
        return self.get_winner() is not None or len(self._moves) == 9

    def get_winner(self):
        return self._winner

    def get_current_player(self):
        if len(self._moves) % 2 == 0:
            return "X"
        return "O"

    def is_cell_empty(self, v, h):
        return self._board[v][h] == " "

    def __str__(self):
        board = self._board
        return ("+---+---+---+\n"
                f"| {board[0][0]} | {board[0][1]} | {board[0][2]} |\n"
                "+---+---+---+\n"
                f"| {board[1][0]} | {board[1][1]} | {board[1][2]} |\n"
                "+---+---+---+\n"
                f"| {board[2][0]} | {board[2][1]} | {board[2][2]} |\n"
                "+---+---+---+")
