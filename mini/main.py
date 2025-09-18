# นำเข้าฟังก์ชัน checkmate จากไฟล์คู่กัน
from checkmate import checkmate

def main():
    # ตัวอย่างที่ 1: จากสเปก
    # R...
    # .K..
    # ..P.
    # ....
    # ในเคสนี้ Pawn (ที่ (2,2)) กินทแยงขึ้นซ้ายไปที่ K (ที่ (1,1)) ได้ => Success
    board1 = """\
             R...
             .K..
             ..P.
             ....\
             """
    checkmate(board1)  # ควรพิมพ์ Success

    # ตัวอย่างที่ 2: กระดาน 2x2
    # ..
    # .K
    # ไม่มีตัวเช็ค => Fail
    board2 = """\
             ..
             .K\
             """
    checkmate(board2)  # ควรพิมพ์ Fail

def run_demo():
    tests = [
        ("spec_example_success", board1, "Success"),
        ("spec_example_fail", board2, "Fail"),
        ("rook_ok", board_rook_ok, "Success"),
        ("rook_block", board_rook_block, "Fail"),
        ("bishop_ok", board_bishop_ok, "Success"),
        ("bishop_block", board_bishop_block, "Fail"),
        ("queen_diag", board_queen_diag, "Success"),
        ("queen_straight", board_queen_straight, "Success"),
        ("pawn_ok", board_pawn_ok, "Success"),
        ("pawn_front_fail", board_pawn_front_fail, "Fail"),
        ("no_king", board_no_king, "Error"),
        ("mixed_fail", board_mixed_fail, "Fail"),
    ]
    for name, b, expect in tests:
        print(f"== {name} ==")
        checkmate(b)        # จะพิมพ์ผลจริงออกมา
        print(f"(expected: {expect})\n")

# เรียกดูผลคร่าวๆ
# run_demo()

# Example 1 จากสเปก → ต้อง Success
board1 = """\
R...
.K..
..P.
....\
"""  # Expected: Success

# Example 2 จากสเปก → ไม่มีตัวโจมตี → Fail
board2 = """\
..
.K\
"""  # Expected: Fail

# Rook ยิงแนวนอนได้ตรงๆ → Success
board_rook_ok = """\
R..K
....
....
....\
"""  # Expected: Success

# Rook มีตัวบัง → Fail
board_rook_block = """\
R.PK
....
....
....\
"""  # Expected: Fail

# Bishop ทแยงถึง → Success
board_bishop_ok = """\
B...
.K..
....
....\
"""  # Expected: Success

# Bishop มีตัวบัง → Fail
board_bishop_block = """\
B...
.P..
..K.
....\
"""  # Expected: Fail

# Queen โจมตีทแยงแบบ Bishop → Success
board_queen_diag = """\
Q...
.K..
....
....\
"""  # Expected: Success

# Queen โจมตีแนวตรงแบบ Rook → Success
board_queen_straight = """\
Q..K
....
....
....\
"""  # Expected: Success

# Pawn โจมตีทแยงขึ้นโดน King → Success
board_pawn_ok = """\
....
.K..
..P.
....\
"""  # Expected: Success

# Pawn อยู่หน้าตรงๆ ไม่ได้กินตรง → Fail
board_pawn_front_fail = """\
....
.K..
.P..
....\
"""  # Expected: Fail

# ไม่มี King เลย → Error
board_no_king = """\
R...
....
..P.
....\
"""  # Expected: Error

# บอร์ดรวมหลายตัว แต่ไม่มีใครถึง King → Fail
board_mixed_fail = """\
R...
..B.
..K.
Q...\
"""  # Expected: Fail


if __name__ == "__main__":
    # เรียก main เมื่อรันไฟล์นี้โดยตรง
    main()
    run_demo()
