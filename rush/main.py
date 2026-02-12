#!/usr/bin/env python3
from checkmate import checkmate

def main():
    # ทดสอบกระดาน
    board = """\
..P.
....
..K.
....\
"""
    checkmate(board)

if __name__ == "__main__":
    main()  