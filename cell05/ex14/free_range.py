#!/usr/bin/env python3
import sys

params = sys.argv[1:]
if len(params) != 2:
    print("none")
else:
    numbers = list( range( int(params[0]), int(params[1]) + 1 ))
    print(numbers)