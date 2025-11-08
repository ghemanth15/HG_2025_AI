# %%
'''
Homework 1 about Conditionals: Write a program that receives an integer from the user and prints
Large if that number is greater than or equal to 100, prints average if that number is between 20 and 100,
and prints Small if that number is less than or equal to 20. You can get an input from user and convert
it to an integer using a = int(input('Please enter an integer:')).
'''

a = int(input('Please enter an integer:'))
if a <= 20:
    print('Small')
elif a>20 and a<100:
    print('Average')
else:
    print('Large')
#Alternative
'''
if a <= 20:
    print('Small')
elif a >= 100:
    print('Large')
else:
    print('Average')
'''

# %%
'''
Homework 2 about Conditionals: Write a program that receives an integer from the user and prints Positive 
Even, Positive Odd, Negative Even, or Negative Odd, depending on the number. You can get an input from user 
and convert it to an integer using a = int(input('Please enter an integer:')).
'''

a = int(input('Please enter an integer:'))
if a < 0 and a%2 == 0:
    print('Negative Even')
elif a < 0 and a%2 == 1:
    print('Negative Odd')
elif a > 0 and a%2 == 0:
    print('Positive Even')
elif a > 0 and a%2 == 1:
    print('Positive Odd')


# %%
'''
Homework 3 about Conditionals: Write a program that asks the user for their exam score (0–100) 
and prints the letter grade: A (90–100), B (80–89), C (70–79), D (60–69), or F (below 60).
'''
score = int(input("Enter your exam score (0-100): "))

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")


# %%
'''
Homework 4 about Conditionals: Write a program that asks for the year and prints "Leap Year" 
if it is divisible by 4 but not by 100, OR divisible by 400. Otherwise, print "Not a Leap Year".
'''
year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")



# %%
'''
Homework 5 about Conditionals: Write a program that asks the user for a temperature in Celsius. 
If temperature is less than 0, print "Freezing". If between 0 and 30, print "Normal". 
If greater than or equal to 30, print "Hot".
'''
temp = float(input("Enter temperature in Celsius: "))

if temp < 0:
    print("Freezing")
elif temp < 30:
    print("Normal")
else:
    print("Hot")


# %%
'''
Homework 6 about Conditionals: Write a program that asks the user to enter three integers. 
Print the largest number among them using conditionals.
'''
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Largest is:", a)
elif b >= a and b >= c:
    print("Largest is:", b)
else:
    print("Largest is:", c)


# %%
'''
Homework 7 about Conditionals: Write a program that asks the user to enter a character. 
Check whether it is a vowel (a, e, i, o, u) or a consonant.
'''
ch = input("Enter a single character: ").lower()

if ch in ['a','e','i','o','u']:
    print("Vowel")
elif ch.isalpha():
    print("Consonant")
else:
    print("Not a letter")



# %%

'''
Homework 8 about Conditionals: Write a program that receives an integer from the user and checks 
if it is divisible by both 3 and 5, only by 3, only by 5, or by neither.
'''
num = int(input("Enter an integer: "))

if num % 3 == 0 and num % 5 == 0:
    print("Divisible by both 3 and 5")
elif num % 3 == 0:
    print("Divisible by 3")
elif num % 5 == 0:
    print("Divisible by 5")
else:
    print("Not divisible by 3 or 5")


# %%
'''
Homework 9 about Conditionals: Write a program that asks for the user’s age. 
If age < 13, print "Child". If 13–19, print "Teenager". If 20–64, print "Adult". If 65 or more, print "Senior".
'''
age = int(input("Enter your age: "))

if age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
elif age < 65:
    print("Adult")
else:
    print("Senior")


# %%
'''
Homework 10 about Conditionals: Write a program that asks the user for two integers 
and prints whether the first is greater, smaller, or equal to the second.
'''
x = int(input("Enter first integer: "))
y = int(input("Enter second integer: "))

if x > y:
    print("First is greater")
elif x < y:
    print("First is smaller")
else:
    print("Both are equal")

