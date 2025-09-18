#!/usr/bin/env python3
import sys
from checkmate import checkmate

def run_one(path: str):
    try:
        with open(path, "r", encoding="utf-8") as f:
            board_str = f.read()
    except Exception:
        print("Error")

    checkmate(board_str)

def main():
    if len(sys.argv) < 2:
        print("Error")

    exit_code = 0
    for path in sys.argv[1:]:
        run_one(path)

main()
