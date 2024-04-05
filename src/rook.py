from src.piece import Piece



class Rook(Piece):
    def char(self):
        return 'R'


    def can_move(self, board, row: int, col: int, row_1: int, col_1: int) -> bool:
        if col != col_1 and row != row_1:
            return False

        elif col==col_1:
            diff_row=abs(row-row_1)

            if row>row_1:
                for i in range(diff_row-1):
                    if board.get_piece(row-i, col) is not None:
                        return False
            else:
                for i in range(diff_row-1):
                    if board.get_piece(row+i, col) is not None:
                        return False

        else:
            diff_col=col-col_1

            if col>col_1:
                for i in range(diff_col-1):
                    if board.get_piece(row, col-i) is not None:
                        return False

            else:
                for i in range(diff_col+1):
                    if board.get_piece(row, col+i) is not None:
                        return False
        return True
    def can_attack (self, board, row: int, col: int, row_1:int, col_1: int) -> bool:
        return self.can_move(self, board, row, col, row_1, col_1)
