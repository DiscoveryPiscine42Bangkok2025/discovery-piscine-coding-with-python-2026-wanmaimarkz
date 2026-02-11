#!/usr/bin/env python3
import sys

def shrink(text):
    print(text[:8])

def enlarge(text):
    print(text + ('Z' * (8 - len(text))))

params = sys.argv[1:]
if not params:
    print("none")
else:
    for i in params:
        if (len(i) > 8 ):
            shrink(i)
        elif (len(i) < 8):
            enlarge(i)
        else:
            print(i)