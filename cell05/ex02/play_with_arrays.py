#!/usr/bin/env python3
numbers = [2, 8, 9, 48, 8, 22, -12, 2]
new_nums = [ i+2 for i in numbers if i > 5]
print(f'{numbers}\n{new_nums}')