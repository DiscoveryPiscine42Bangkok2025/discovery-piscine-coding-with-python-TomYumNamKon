#!/usr/bin/env python3
import sys

if len(sys.argv) != 2:
    print("none")
else:
    s = sys.argv[1]
    found = False
    for ch in s:
        if ch == "z":
            print("z")
            found = True
    if not found:
        print("none")