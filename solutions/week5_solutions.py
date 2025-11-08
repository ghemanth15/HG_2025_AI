# %%
'''
Homework 1 about Integers and Floats: Write a program that receives an integer from the user, called n,
and prints the first n prime numbers. For example, if the input is 7, the output should
be: 2, 3, 5, 7, 11, 13, 17.
'''

def isprime(x):
    if x <= 1:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

def n_first_prime(n):
    c = 2
    while n != 0:
        if isprime(c):
            print(c, end=', ')
            n -= 1
        c += 1

n = int(input("Enter a number: "))
n_first_prime(n)

# %%
'''
Homework 2 about Integers and Floats: Write a program that receives an integer n
and prints whether it is a prime number.
For example, if n = 13, the output should be: Prime
'''

n = int(input("Enter an integer: "))
if n > 1:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")
else:
    print("Not Prime")


# %%
'''
Homework 3 about Integers and Floats: Write a program that receives an integer n
and prints the reverse of that number.
For example, if n = 1234, the output should be: 4321
'''

n = int(input("Enter an integer: "))
rev = 0
temp = abs(n)
while temp > 0:
    rev = rev * 10 + temp % 10
    temp //= 10
print("Reversed:", rev if n >= 0 else -rev)


# %%
'''
Homework 4 about Integers and Floats: Write a program that receives a float number
and prints its square root rounded to 3 decimal places.
'''

import math

x = float(input("Enter a float number: "))
print("Square root:", round(math.sqrt(x), 3))


# %%
'''
Homework 5 about Integers and Floats: Write a program that receives an integer n
and prints the sum of the cubes of the first n natural numbers.
For example, if n = 3, the output should be 1^3 + 2^3 + 3^3 = 36.
'''

n = int(input("Enter an integer: "))
total = 0
for i in range(1, n+1):
    total += i**3
print("Sum of cubes up to", n, "is:", total)


# %%
'''
Homework 6 about Integers and Floats: Write a program that receives two integers a and b
and prints their least common multiple (LCM).
For example, if a=12 and b=18, the output should be: 36
'''

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))
lcm = abs(a*b) // gcd(a, b) if a and b else 0
print("LCM is:", lcm)

# %%
'''
Homework 7 about Integers and Floats: Write a program that receives a float number
and prints it rounded to the nearest integer without using round().
(Hint: add 0.5 and take int for positives; subtract 0.5 for negatives.)
'''

x = float(input("Enter a float number: "))
if x >= 0:
    nearest = int(x + 0.5)
else:
    nearest = int(x - 0.5)
print("Nearest integer:", nearest)


# %%
'''
Homework 8 about Integers and Floats: Write a program that receives an integer n
and prints the binary, octal, and hexadecimal representations of that number.
For example, if n = 25, output should be: 11001, 31, 19
'''

n = int(input("Enter an integer: "))
print("Binary:", bin(n)[2:])
print("Octal:", oct(n)[2:])
print("Hexadecimal:", hex(n)[2:])


# %%
'''
Homework 9 about Integers and Floats: Write a program that receives two integers a and b
and prints the power a^b (a raised to b) without using the ** operator.
'''

a = int(input("Enter base integer: "))
b = int(input("Enter exponent integer: "))
result = 1
for _ in range(abs(b)):
    result *= a
result = result if b >= 0 else 1 / result
print("Result:", result)

# %%
'''
Homework 10 about Integers and Floats: Write a program that receives a float distance in kilometers
and converts it to miles. (1 km = 0.621371 miles)
'''

km = float(input("Enter distance in kilometers: "))
miles = km * 0.621371
print("Miles:", round(miles, 3))
