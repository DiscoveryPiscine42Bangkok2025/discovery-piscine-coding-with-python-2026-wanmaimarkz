#!/usr/bin/env python3
import sys
import re

params = sys.argv[1:]
if len(params) != 2:
    print("none")
else:
    print(len(re.findall(params[0], params[1])))