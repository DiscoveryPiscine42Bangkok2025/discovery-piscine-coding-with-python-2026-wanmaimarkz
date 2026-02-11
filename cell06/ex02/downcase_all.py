#!/usr/bin/env python3
import sys

def downcase_it(text):
    """Returns the string converted to lowercase."""
    return text.lower()


params = sys.argv[1:]
if not params:
    print("none")
else:
    for i in params:
        print(downcase_it(i))
