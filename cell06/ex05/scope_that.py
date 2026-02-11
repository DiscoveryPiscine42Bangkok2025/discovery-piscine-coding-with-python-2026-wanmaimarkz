#!/usr/bin/env python3
def add_one(x):
    """Adds 1 to the parameter passed to the method."""
    x = x + 1

my_var = 42

print(f"Before: {my_var}")
add_one(my_var)
print(f"After:  {my_var}")