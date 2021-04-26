import unittest
from board import Board, InvalidMoveError


class TestBoard(unittest.TestCase):
    def test_is_cell_empty(self):
        board = Board()

        self.assertTrue(board.is_cell_empty(0, 0))

        board.make_move(0, 0)

        self.assertFalse(board.is_cell_empty(0, 0))
        self.assertTrue(board.is_cell_empty(0, 1))

    def test_get_current_player(self):
        board = Board()

        self.assertEqual(board.get_current_player(), "X")

        board.make_move(2, 2)

        self.assertEqual(board.get_current_player(), "O")

        board.make_move(1, 1)

        self.assertEqual(board.get_current_player(), "X")

    def test_get_winner(self):
        board = Board()

        self.assertIsNone(board.get_winner())

        board.make_move(0, 0)
        board.make_move(0, 1)
        board.make_move(1, 1)
        board.make_move(0, 2)

        self.assertIsNone(board.get_winner())

        board.make_move(2, 2)

        self.assertEqual(board.get_winner(), "X")

    def test_is_game_over(self):
        board = Board()

        self.assertFalse(board.is_game_over())
        self.assertIsNone(board.get_winner())

        board.make_move(0, 0)
        board.make_move(0, 1)
        board.make_move(1, 1)
        board.make_move(0, 2)

        self.assertFalse(board.is_game_over())
        self.assertIsNone(board.get_winner())

        board.make_move(2, 2)

        self.assertTrue(board.is_game_over())
        self.assertEqual(board.get_winner(), "X")

    def test_is_game_over_without_winner(self):
        board = Board()

        self.assertFalse(board.is_game_over())
        self.assertIsNone(board.get_winner())

        board.make_move(1, 1)
        board.make_move(0, 2)
        board.make_move(0, 1)
        board.make_move(2, 1)
        board.make_move(0, 0)
        board.make_move(2, 2)
        board.make_move(1, 2)
        board.make_move(1, 0)

        self.assertFalse(board.is_game_over())
        self.assertIsNone(board.get_winner())

        board.make_move(2, 0)

        self.assertTrue(board.is_game_over())
        self.assertIsNone(board.get_winner())

    def test_str(self):
        board = Board()

        self.assertEqual(
            str(board),
            (
                "+---+---+---+\n"
                "|   |   |   |\n"
                "+---+---+---+\n"
                "|   |   |   |\n"
                "+---+---+---+\n"
                "|   |   |   |\n"
                "+---+---+---+"
            ),
        )

        board.make_move(1, 0)
        board.make_move(1, 1)
        board.make_move(1, 2)

        self.assertEqual(
            str(board),
            (
                "+---+---+---+\n"
                "|   |   |   |\n"
                "+---+---+---+\n"
                "| X | O | X |\n"
                "+---+---+---+\n"
                "|   |   |   |\n"
                "+---+---+---+"
            ),
        )

    def test_raise_exception_if_cell_is_not_empty(self):
        board = Board()
        board.make_move(0, 0)

        self.assertFalse(board.is_cell_empty(0, 0))

        with self.assertRaises(InvalidMoveError) as ctx:
            board.make_move(0, 0)
        self.assertEqual(str(ctx.exception), "Cell (1, 1) is already occupied.")

    def test_raise_exception_if_game_is_over(self):
        board = Board()
        board.make_move(0, 0)
        board.make_move(0, 1)
        board.make_move(1, 1)
        board.make_move(0, 2)
        board.make_move(2, 2)

        self.assertTrue(board.is_game_over())

        with self.assertRaises(InvalidMoveError) as ctx:
            board.make_move(2, 1)
        self.assertEqual(str(ctx.exception), "Game is already over.")


if __name__ == "__main__":
    unittest.main()
