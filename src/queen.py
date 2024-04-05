from src.piece import Piece



class Queen(Piece):
    def char(self):
        return 'Q'

    def can_move(self, board, row: int, col: int, row_1: int, col_1: int) -> bool:
        diff_col=abs(col-col_1)
        diff_row=abs(row-row_1)

        if diff_col==0:
            if row>row_1:
                for i in range(diff_row-1):
                    if board.get_piece(row-i, col) is not None:
                        return False
            else:
                for i in range(diff_row-1):
                    if board.get_piece(row+i, col) is not None:
                        return False
        elif diff_row==0:
            if col>col_1:
                for i in range(diff_col-1):
                    if board.get_piece(row, col-i) is not None:
                        return False

            else:
                for i in range(diff_col+1):
                    if board.get_piece(row, col+i) is not None:
                        return False

        elif diff_row!=diff_col:
            return False

        else:
            if row-row_1 > 0 and col-col_1 > 0:
                for i in range(diff_row-1):
                    if board.get_piece(row-i, col-i) is not None:
                        return False

            elif row-row_1 > 0 and col-col_1 < 0:
                for i in range(diff_row-1):
                    if board.get_piece(row-i, col+i) is not None:
                        return False

            elif row-row_1 < 0 and col-col_1 < 0:
                for i in range(diff_row-1):
                    if board.get_piece(row+i, col+i) is not None:
                        return False

            else:
                for i in range(diff_row-1):
                    if board.get_piece(row+i, col-i) is not None:
                        return False
        return True

    def can_attack (self, board, row: int, col: int, row_1:int, col_1: int) -> bool:
        return self.can_move(self, board, row, col, row_1, col_1)
