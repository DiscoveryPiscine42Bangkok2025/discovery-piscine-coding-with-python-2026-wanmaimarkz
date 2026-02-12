def checkmate(board):
    # 1. แปลงสตริงเป็น list ของบรรทัด และตัดบรรทัดว่างทิ้ง
    rows = [r for r in board.split('\n') if len(r) > 0]
    
    # 2. เช็ก Error พื้นฐาน (ไม่มีข้อมูล หรือ กระดานไม่เป็นจัตุรัส)
    if not rows:
        print("Error 'Empty board'")
        return
    
    size = len(rows)
    for row in rows:
        if len(row) != size:
            print("Error 'board is not square'")
            return

    # 3. หาตำแหน่ง King (K) และเก็บตำแหน่งตัวหมากฝ่ายตรงข้าม
    king_pos = None
    pieces = []
    
    for r in range(size):
        for c in range(size):
            char = rows[r][c]
            if char == 'K':
                if king_pos: # ถ้าเจอ King เกิน 1 ตัว
                    print("Error 'More than 1 king in board'")
                    return
                king_pos = (r, c)
            elif char in "PBRQ": # เก็บเฉพาะตัวหมากที่รู้จัก
                pieces.append((char, r, c))
    
    # ถ้าหา King ไม่เจอเลย
    if not king_pos:
        print("Error 'No king in board'")
        return

    kr, kc = king_pos

    # 4. ฟังก์ชันเช็กว่าทางโล่งไหม (เดินจากชิ้นส่วน -> หา King)
    def is_path_clear(r1, c1, r2, c2):
        # หา step การเดิน (-1, 0, หรือ 1)
        step_r = 0
        if r2 > r1: step_r = 1
        elif r2 < r1: step_r = -1
            
        step_c = 0
        if c2 > c1: step_c = 1
        elif c2 < c1: step_c = -1
            
        # เริ่มเดินจากช่องถัดไป
        curr_r, curr_c = r1 + step_r, c1 + step_c
        while (curr_r, curr_c) != (r2, c2):
            # ถ้าเจอตัวหมากขวางทาง (P, B, R, Q) ให้ถือว่าไม่โล่ง
            # (ตัวอักษรอื่นถือเป็นช่องว่าง ไม่บังทาง)
            if rows[curr_r][curr_c] in "PBRQ":
                return False
            curr_r += step_r
            curr_c += step_c
        return True

    # 5. วนลูปเช็กว่าตัวหมากตัวไหนกิน King ได้บ้าง
    for p_type, pr, pc in pieces:
        # คำนวณระยะห่าง
        diff_r = kr - pr
        diff_c = kc - pc
        
        can_attack = False
        
        # --- กติกา Pawn (P) ---
        # สมมติ P โจมตีขึ้นบน (row ของ King ต้องน้อยกว่า row ของ Pawn)
        if p_type == 'P':
            if diff_r == -1 and abs(diff_c) == 1:
                can_attack = True
                
        # --- กติกา Rook (R) ---
        # แนวตรง (แถวเดียวกัน หรือ หลักเดียวกัน)
        elif p_type == 'R':
            if diff_r == 0 or diff_c == 0:
                if is_path_clear(pr, pc, kr, kc):
                    can_attack = True
                    
        # --- กติกา Bishop (B) ---
        # แนวทแยง (ระยะห่างแนวนอน เท่ากับ ระยะห่างแนวตั้ง)
        elif p_type == 'B':
            if abs(diff_r) == abs(diff_c):
                if is_path_clear(pr, pc, kr, kc):
                    can_attack = True
                    
        # --- กติกา Queen (Q) ---
        # เป็นได้ทั้ง R และ B
        elif p_type == 'Q':
            is_straight = (diff_r == 0 or diff_c == 0)
            is_diagonal = (abs(diff_r) == abs(diff_c))
            
            if is_straight or is_diagonal:
                if is_path_clear(pr, pc, kr, kc):
                    can_attack = True
        
        # ถ้าเจอตัวไหนโจมตีได้ ให้จบเลย
        if can_attack:
            print("Success")
            return

    # ถ้าวนครบทุกตัวแล้วไม่มีใครทำอะไร King ได้
    print("Fail")
