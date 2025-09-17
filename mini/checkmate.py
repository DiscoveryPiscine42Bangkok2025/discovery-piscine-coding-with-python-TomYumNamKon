# นำเข้าประเภทข้อมูลที่ช่วยเรื่อง type hints (ไม่บังคับ แต่ทำให้โค้ดอ่านง่าย)
from typing import List, Tuple, Optional

def _parse_board(board_text: str) -> List[List[str]]:
    # แยกสตริงทั้งบอร์ดเป็นบรรทัด โดยตัดช่องว่างหัวท้าย
    lines = [line for line in board_text.strip().splitlines() if line.strip() != ""]
    # ตรวจว่ามีอย่างน้อย 1 แถว
    if not lines:
        raise ValueError("Empty board")
    # ขนาด N ของบอร์ด (ต้องเป็นสี่เหลี่ยมจัตุรัส N x N)
    n = len(lines)
    # ตรวจทุกแถวว่าความยาวเท่ากับ N
    for row in lines:
        if len(row) != n:
            raise ValueError("Board must be square")
    # แปลงเป็น list ของ list ตัวอักษร เพื่อเข้าถึงด้วย index ได้ง่าย
    grid = [list(row) for row in lines]
    return grid

def _find_king(grid: List[List[str]]) -> Tuple[int, int]:
    # หาตำแหน่ง King ('K') บนกระดาน
    positions = []
    for r, row in enumerate(grid):
        for c, ch in enumerate(row):
            if ch == 'K':
                positions.append((r, c))
    # ต้องมี King เพียงตัวเดียว
    if len(positions) != 1:
        raise ValueError("There must be exactly one King")
    return positions[0]

def _in_bounds(r: int, c: int, n: int) -> bool:
    # เช็คว่า index (r,c) อยู่ในขอบเขตบอร์ดหรือไม่
    return 0 <= r < n and 0 <= c < n

def _ray_hits_king(grid: List[List[str]], start: Tuple[int, int], dr: int, dc: int, king_pos: Tuple[int, int]) -> bool:
    # ไล่ตามแนว (dr, dc) จากจุด start ไปเรื่อย ๆ เพื่อดูว่าชน K เป็นชิ้นแรกหรือไม่
    n = len(grid)                       # ขนาดบอร์ด
    r, c = start                        # เริ่มต้นที่ตำแหน่งของตัวหมาก
    r += dr                             # ขยับหนึ่งก้าวตามทิศ
    c += dc                             # ขยับหนึ่งก้าวตามทิศ
    while _in_bounds(r, c, n):          # วนจนกว่าจะหลุดบอร์ด
        ch = grid[r][c]                 # ตัวอักษรที่ช่องปัจจุบัน
        if ch == 'K':                   # ถ้าเจอ King ก่อนเจออะไรกั้น
            return True                 # ถือว่าเช็คได้
        if ch in ('P', 'B', 'R', 'Q'):  # ถ้าเจอหมากอื่นขวาง
            return False                # เส้นนี้ถูกบล็อก
        # อักขระอื่น ๆ ถือว่าเป็นช่องว่าง (รวมถึง '.' หรืออื่น ๆ)
        r += dr                         # เดินต่อไปทิศเดิม
        c += dc                         # เดินต่อไปทิศเดิม
    return False                        # เดินสุดทางแล้วไม่เจอ King

def _pawn_checks_king(grid: List[List[str]], pawn_pos: Tuple[int, int], king_pos: Tuple[int, int]) -> bool:
    # กำหนดทิศการกินของ Pawn: สมมติศัตรู (P) เดินจากล่างขึ้นบน (แถวเพิ่ม -> ลด)
    # จากตัวอย่างในสเปก P ที่อยู่ข้างล่างสามารถกินทแยงขึ้นซ้าย/ขวาไปหา K ได้
    pr, pc = pawn_pos                   # ตำแหน่ง Pawn
    kr, kc = king_pos                   # ตำแหน่ง King
    # ช่องที่ Pawn กินได้คือ (pr-1, pc-1) และ (pr-1, pc+1) ถ้าอยู่ในบอร์ด
    targets = [(pr - 1, pc - 1), (pr - 1, pc + 1)]
    # ถ้าใด ๆ เท่ากับตำแหน่ง King ก็ถือว่าเช็ค
    return (kr, kc) in targets

def is_king_in_check(board_text: str) -> bool:
    # ฟังก์ชันหลัก: รับข้อความบอร์ด แล้วบอกว่า King โดนเช็คหรือไม่ (True/False)
    grid = _parse_board(board_text)     # แปลงข้อความเป็นตาราง
    n = len(grid)                       # ขนาดบอร์ด N
    k_r, k_c = _find_king(grid)         # หาตำแหน่ง King

    # ทิศของ Bishop/Diagonal (รวมถึง Queen ในแนวทแยง)
    diag_dirs = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    # ทิศของ Rook/Orthogonal (รวมถึง Queen ในแนวตรง)
    ortho_dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # วนหาหมากทั้งหมดบนกระดาน
    for r in range(n):
        for c in range(n):
            ch = grid[r][c]             # ตัวอักษรในช่อง (r,c)
            if ch == 'P':
                # Pawn: เช็คแบบกินทแยงขึ้น
                if _pawn_checks_king(grid, (r, c), (k_r, k_c)):
                    return True
            elif ch == 'B':
                # Bishop: ไล่สี่ทิศทแยง ถ้าเจอ K ก่อนโดนบล็อก => เช็ค
                for dr, dc in diag_dirs:
                    if _ray_hits_king(grid, (r, c), dr, dc, (k_r, k_c)):
                        return True
            elif ch == 'R':
                # Rook: ไล่สี่ทิศตรง
                for dr, dc in ortho_dirs:
                    if _ray_hits_king(grid, (r, c), dr, dc, (k_r, k_c)):
                        return True
            elif ch == 'Q':
                # Queen: รวมทั้งทแยงและตรง
                for dr, dc in diag_dirs + ortho_dirs:
                    if _ray_hits_king(grid, (r, c), dr, dc, (k_r, k_c)):
                        return True
            # อักขระอื่น ๆ ไม่ใช่หมาก (ถือว่าเป็นช่องว่าง) ข้ามไป
    # ถ้าวนหมดแล้วไม่เจอการเช็ค => False
    return False

def checkmate(board_text: str) -> None:
    # Wrapper ตามสเปก: พิมพ์ "Success" ถ้าโดนเช็ค ไม่งั้น "Fail"
    try:
        # เรียกตรวจ
        in_check = is_king_in_check(board_text)
        # พิมพ์ตามผลลัพธ์
        print("Success" if in_check else "Fail")
    except Exception:
        # เงื่อนไข error: พิมพ์ "Error" ตามตัวอย่างสเปก
        print("Error")
