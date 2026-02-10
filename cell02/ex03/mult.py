print("Enter the first number:")
num1 = int(input())
print("Enter the second number:")
num2 = int(input())

result = num1 * num2

if result > 0 :
    print(f'{num1} X {num2} = {result}\nThe result is positive.')
elif result < 0:
    print(f'{num1} X {num2} = {result}\nThe result is Negative.')
else:
    print(f'{num1} X {num2} = {result}\nThe result is positive and negative.')