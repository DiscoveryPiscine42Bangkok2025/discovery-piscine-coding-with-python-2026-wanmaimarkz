#!/usr/bin/env python3
num1 = int(input("Give me the first number: "))
num2 = int(input("Give me the second number: "))
print("Thank you!")

if ((num1!=0 and num2 == 0) or (num1==0 and num2 == 0)):
    print("ZeroDivisionError: can't devided by zero!")
else:
    print(f"{num1} + {num2} = { num1 + num2 }\n{num1} - {num2} = { num1 - num2 }\n{num1} / {num2} = { int(num1 / num2)}\n{num1} * {num2} = { num1 * num2 }")