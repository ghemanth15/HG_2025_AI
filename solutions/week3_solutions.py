# %%
'''
Homework 1 about Functions: Write a function that receives two numbers as parameters and returns their
multiplication. Call that function and print its output. For instance, if the arguments are 3 and 5,
the output should be 15.
'''

def multip(a, b):
    return a * b

print('The result of the multiplication is:', multip(3, 5))


# %%
'''
Homework 2 about Functions: Write a function that receives three parameters: name, weight, and height.
The default value for name is James. The function calculates the BMI. BMI is: weight/(height^2).
Weight should be in kg and height should be in meters. For instance, if the weight is 60 kg and the
height is 1.7 m, then the BMI should be 20.76. The function should return "<name>'s BMI is greater
than or equal to 22" if the BMI is greater than or equal to 22. Otherwise, return "<name>'s BMI is less than 22".
Call the function and print its output.
'''

def BMI_cal(weight, height, name='James'):
    bmi = weight / (height ** 2)
    if bmi >= 22:
        return f"{name}'s BMI is greater than or equal to 22"
    else:
        return f"{name}'s BMI is less than 22"

output = BMI_cal(name='John', weight=60, height=1.7)
print(output)


# %%
'''
Homework 3 about Functions: Write a function that receives a string as input and returns the number of vowels in it.
Call the function and print the result for at least two sample strings.
'''

def count_vowels(text):
    vowels = "aeiouAEIOU"
    return sum(1 for ch in text if ch in vowels)

print("Vowel count:", count_vowels("Hello World"))
print("Vowel count:", count_vowels("Graduate Students"))


# %%
'''
Homework 4 about Functions: Write a function that receives an integer n and returns the factorial of n.
Call the function for n = 5 and n = 7 and print the results.
'''

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print("Factorial of 5:", factorial(5))
print("Factorial of 7:", factorial(7))


# %%
'''
Homework 5 about Functions: Write a function that receives a list of numbers and returns the maximum and minimum values.
Call the function with a sample list and print the results.
'''

def find_min_max(numbers):
    return min(numbers), max(numbers)

nums = [12, 5, 7, 25, 3, 19]
mn, mx = find_min_max(nums)
print("Minimum:", mn, "Maximum:", mx)


# %%
'''
Homework 6 about Functions: Write a function that takes a list of numbers and returns a new list with only the even numbers.
Call the function and print the returned list.
'''

def filter_even(numbers):
    return [n for n in numbers if n % 2 == 0]

print("Even numbers:", filter_even([1, 2, 3, 4, 5, 6, 7, 8, 9]))


# %%
'''
Homework 7 about Functions: Write a recursive function that calculates the nth Fibonacci number.
Call the function for n = 5 and n = 10 and print the results.
'''

def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

print("Fibonacci(5):", fib(5))
print("Fibonacci(10):", fib(10))


# %%
'''
Homework 8 about Functions: Write a function that accepts any number of integer arguments (*args)
and returns their average. Call the function with 3, 5, 7 and with 10, 20, 30, 40.
'''

def average(*args):
    return sum(args) / len(args)

print("Average:", average(3, 5, 7))
print("Average:", average(10, 20, 30, 40))


# %%
'''
Homework 9 about Functions: Write a function that accepts a dictionary of student names and their scores.
The function should return the name of the student with the highest score.
'''

def top_student(scores):
    return max(scores, key=scores.get)

students = {"Alice": 88, "Bob": 95, "Charlie": 90}
print("Top student:", top_student(students))


# %%
'''
Homework 10 about Functions: Write a function that checks if a given string is a palindrome (the same forwards and backwards).
Call the function with at least two examples and print the results.
'''

def is_palindrome(text):
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]

print("Is 'madam' a palindrome?", is_palindrome("madam"))
print("Is 'Graduate Level' a palindrome?", is_palindrome("Graduate Level"))