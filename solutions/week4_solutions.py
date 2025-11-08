# %%
'''
Homework 1 about Integers and Floats: Write a program that receives an integer, greater than or equal
to 2, from the user and prints whether that number is odd or even.
'''

num = int(input('Please enter an integer: '))
if num % 2 == 0:
    print('even')
else:
    print('odd')


# %%
'''
Homework 2 about Integers and Floats: The Fibonacci Sequence is a series of numbers. The first two numbers
are 0 and 1. The next number is found by adding up the two numbers before it.
For example, 0, 1, 1, 2, 3, 5, 8, 13, 21. The next number in this series is 13+21 = 34. Write a program
that receives an integer from the user, called n, and prints out Fibonacci series up to n terms.
'''

n = int(input('Please enter an integer: '))
i, j = 0, 1
print(i)
print(j)
for _ in range(n - 2):
    fib = i + j
    print(fib)
    i, j = j, fib


# %%
'''
Homework 3 about Integers and Floats: Write a program that receives an integer n
and prints whether the number is a palindrome (reads the same backward and forward).
For example, n = 121 → Palindrome; n = 123 → Not Palindrome.
'''

n = int(input("Enter an integer: "))
s = str(abs(n))
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")


# %%
'''
Homework 4 about Integers and Floats: Write a program that receives two float numbers from the user
and prints their sum, difference, product, and quotient with results rounded to 2 decimal places.
'''

a = float(input("Enter first float: "))
b = float(input("Enter second float: "))

print("Sum:", round(a + b, 2))
print("Difference:", round(a - b, 2))
print("Product:", round(a * b, 2))
print("Quotient:", round(a / b, 2) if b != 0 else "Division by zero not allowed")


# %%
'''
Homework 5 about Integers and Floats: Write a program that receives an integer n from the user and prints
the sum of squares of the first n natural numbers.
For example, if n=3, the output should be 1^2 + 2^2 + 3^2 = 14.
'''

n = int(input("Enter a positive integer: "))
total = 0
for i in range(1, n + 1):
    total += i ** 2
print("Sum of squares up to", n, "is:", total)


# %%
'''
Homework 6 about Integers and Floats: Write a program that calculates the area and circumference of a circle
given its radius as input (a float).
'''

import math

r = float(input("Enter the radius: "))
area = math.pi * r ** 2
circumference = 2 * math.pi * r
print("Area:", round(area, 2))
print("Circumference:", round(circumference, 2))


# %%
'''
Homework 7 about Integers and Floats: Write a program that receives a float number from the user
and prints its floor and ceiling values without using math.floor() or math.ceil().
(Hint: Use int casting and condition checks).
'''

x = float(input("Enter a float number: "))
floor_val = int(x) if x >= 0 else int(x) - 1
ceil_val = int(x) if x == int(x) else int(x) + 1 if x > 0 else int(x)
print("Floor:", floor_val, "Ceiling:", ceil_val)


# %%
'''
Homework 8 about Integers and Floats: Write a program that converts a temperature given in Celsius
to both Fahrenheit and Kelvin.
'''

celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
kelvin = celsius + 273.15
print("Fahrenheit:", round(fahrenheit, 2))
print("Kelvin:", round(kelvin, 2))


# %%
'''
Homework 9 about Integers and Floats: Write a program that receives an integer n and computes the sum of its digits.
For example, if n = 753, the output should be 15.
'''

n = int(input("Enter an integer: "))
digit_sum = 0
temp = abs(n)
while temp > 0:
    digit_sum += temp % 10
    temp //= 10
print("Sum of digits:", digit_sum)


# %%
'''
Homework 10 about Integers and Floats: Write a program that receives two integers a and b,
and prints the greatest common divisor (GCD) using the Euclidean algorithm.
'''

a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))

while b != 0:
    a, b = b, a % b
print("GCD is:", a)