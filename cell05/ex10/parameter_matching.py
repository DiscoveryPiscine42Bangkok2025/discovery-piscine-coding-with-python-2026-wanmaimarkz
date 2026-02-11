#!/usr/bin/env python3
import sys

params = sys.argv[1:]
if len(params) != 1:
    print("none")
else:
    text = input("What was the parameter? ")
    if (text == params[0]):
        print("Good job!")
    else:
        print("Nope, sorry...")