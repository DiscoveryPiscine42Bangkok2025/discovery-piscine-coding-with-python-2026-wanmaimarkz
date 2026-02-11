#!/usr/bin/env python3
import sys

params = sys.argv[1:]
if len(params) < 1:
    print("none")
else:
    end_txt = "ism"
    for i in params:
        if not i.endswith(end_txt):
            print(i + end_txt)