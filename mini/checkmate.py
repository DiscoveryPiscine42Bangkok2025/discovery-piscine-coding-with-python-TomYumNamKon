#!/usr/bin/env python3

class Piece:
    def __init__(self, x, y):         # <-- แก้ให้เป็น (x, y) ตาม row, col
        self.x = x
        self.y = y
    
    def can_attack(self, king, board):
        return False


class King(Piece):
    def __init__(self, x, y):
        super().__init__(x, y)


class Rook(Piece):
    def __init__(self, x, y):
        super().__init__(x, y)

    def can_attack(self, king, board):
        # แนวนอน (row เดียวกัน)
        if self.x == king.x:
            step = 1 if king.y > self.y else -1
            for j in range(self.y + step, king.y, step):
                if board[self.x][j] != ".":      # มีตัวบัง
                    return False
            return True
        # แนวตั้ง (col เดียวกัน)
        if self.y == king.y:
            step = 1 if king.x > self.x else -1
            for i in range(self.x + step, king.x, step):
                if board[i][self.y] != ".":      # มีตัวบัง
                    return False
            return True
        return False


class Bishop(Piece):
    def __init__(self, x, y):
        super().__init__(x, y)

    def can_attack(self, king, board):
        dx = king.x - self.x
        dy = king.y - self.y
        if abs(dx) != abs(dy):                  # ต้องทแยงเท่านั้น
            return False
        step_x = 1 if dx > 0 else -1
        step_y = 1 if dy > 0 else -1
        i, j = self.x + step_x, self.y + step_y
        while i != king.x and j != king.y:
            if board[i][j] != ".":              # มีตัวบัง
                return False
            i += step_x
            j += step_y
        return True


class Queen(Piece):
    def __init__(self, x, y):
        super().__init__(x, y)

    def can_attack(self, king, board):
        # Queen = Rook ∪ Bishop
        return (Rook(self.x, self.y).can_attack(king, board) or
                Bishop(self.x, self.y).can_attack(king, board))


class Pawn(Piece):
    def __init__(self, x, y):
        super().__init__(x, y)

    def can_attack(self, king, board):
        # โจมตี "ทแยงขึ้น": แถว -1 และคอลัมน์ ±1
        return (king.x, king.y) in [
            (self.x - 1, self.y - 1),
            (self.x - 1, self.y + 1),
        ]


def checkmate(board_str: str):
    board = [list(row.strip()) for row in board_str.strip().split("\n")]
    size = len(board)

    pieces = []
    king = None

    mapping = {"K": King, "R": Rook, "B": Bishop, "Q": Queen, "P": Pawn}

    for i in range(size):
        if(size != len(board[i])):
            print("Error")
            return
        for j in range(size):
            c = board[i][j]
            if c in mapping:
                piece = mapping[c](i, j)   # i=row=x, j=col=y
                if c == "K":
                    king = piece
                else:
                    pieces.append(piece)

    if not king:
        print("Error")
        return

    for p in pieces:
        if p.can_attack(king, board):
            print("Success")
            return

    print("Fail")
