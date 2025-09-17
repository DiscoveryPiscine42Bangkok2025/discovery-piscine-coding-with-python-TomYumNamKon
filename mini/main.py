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

if __name__ == "__main__":
    # เรียก main เมื่อรันไฟล์นี้โดยตรง
    main()
