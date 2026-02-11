#!/usr/bin/env python3
import sys

params = sys.argv[1:]
if len(params) != 1:
    print("none")
else:
    char = 'z'
    count_z = params[0].count(char)
    if count_z > 0:
        print(char * count_z)
    else:
        print("none")