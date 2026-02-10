#!/usr/bin/env python3
print("Enter number less than 25")
num = int(input())
if (num > 25):
    print("Error")
else:
    for num in range(num, 25+1):
        print(f"Inside the loop, my variable is {num}")