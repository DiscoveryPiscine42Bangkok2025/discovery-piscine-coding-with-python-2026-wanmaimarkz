def checkmate(board):
    rows = [r for r in board.split('\n') if len(r) > 0]

    if not rows:
        print("Error 'Empty board'")
        return
    
    size = len(rows)
    for row in rows:
        if len(row) != size:
            print("Error 'board is not square'")
            return

    king_pos = None
    pieces = []
    
    for r in range(size):
        for c in range(size):
            char = rows[r][c]
            if char == 'K':
                if king_pos:
                    print("Error 'More than 1 king in board'")
                    return
                king_pos = (r, c)
            elif char in "PBRQ":
                pieces.append((char, r, c))
    
    if not king_pos:
        print("Error 'No king in board'")
        return

    kr, kc = king_pos

    def is_path_clear(r1, c1, r2, c2):
        step_r = 0
        if r2 > r1: step_r = 1
        elif r2 < r1: step_r = -1
            
        step_c = 0
        if c2 > c1: step_c = 1
        elif c2 < c1: step_c = -1
            
        curr_r, curr_c = r1 + step_r, c1 + step_c
        while (curr_r, curr_c) != (r2, c2):
            if rows[curr_r][curr_c] in "PBRQ":
                return False
            curr_r += step_r
            curr_c += step_c
        return True

    for p_type, pr, pc in pieces:
        diff_r = kr - pr
        diff_c = kc - pc
        
        can_attack = False
        
        if p_type == 'P':
            if diff_r == -1 and abs(diff_c) == 1:
                can_attack = True
                
        elif p_type == 'R':
            if diff_r == 0 or diff_c == 0:
                if is_path_clear(pr, pc, kr, kc):
                    can_attack = True
                    
        elif p_type == 'B':
            if abs(diff_r) == abs(diff_c):
                if is_path_clear(pr, pc, kr, kc):
                    can_attack = True
                    
        elif p_type == 'Q':
            is_straight = (diff_r == 0 or diff_c == 0)
            is_diagonal = (abs(diff_r) == abs(diff_c))
            
            if is_straight or is_diagonal:
                if is_path_clear(pr, pc, kr, kc):
                    can_attack = True
        
        if can_attack:
            print("Success")
            return

    print("Fail")
