#Homework 1 about Conditionals: Write a program that receives an integer from the user and prints
# Large if that number is greater than or equal to 100, prints average if that number is between 20 and 100,
# and prints Small if that number is less than or equal to 20. You can get an input from user and convert
# it to an integer using a = int(input('Please enter an integer:')).
a = int(input('Please enter an integer:'))
if a <= 20:
    print('Small')
elif a>20 and a<100:
    print('Average')
else:
    print('Large')
#Alternative
if a <= 20:
    print('Small')
elif a >= 100:
    print('Large')
else:
    print('Average')

#Homework 2 about Conditionals: Write a program that receives an integer from the user and prints Positive
# Even, Positive Odd, Negative Even, or Negative Odd, depending on the number. You can get an input from user
# and convert it to an integer using a = int(input('Please enter an integer:')).
a = int(input('Please enter an integer:'))
if a < 0 and a%2 == 0:
    print('Negative Even')
elif a < 0 and a%2 == 1:
    print('Negative Odd')
elif a > 0 and a%2 == 0:
    print('Positive Even')
elif a > 0 and a%2 == 1:
    print('Positive Odd')

#Homework 3 about Loops: Write a for loop that iterates through numbers from 1 to 10 using the range
# function, adds them up together, and prints the total. The printed output should be 55.
total = 0
for i in range(1, 11):
    total += i
print('The total is:', total)

#Homework 4 about Loops: Write a program that receives an integer input from the user and call it n. Use a
# for loop and an if condition, to find the summation of all numbers that are not a
# multiple of 3, from 1 to n, including 1 and n and print the result. For instance, the output of your
# program for 9, should be 27 and for 17 should be 108. You can get an input from user and convert it to
# an integer using a = int(input('Please enter an integer:')).
n = int(input('Please enter an integer:'))
total = 0
for i in range(1, n+1):
    if i%3 != 0:
        total += i
print('The total is:', total)

#Homework 5 about Functions: Write a function that receives two numbers as parameters and returns their
# multiplcation. Call that function and print its output. For instance, if the arguments are 3 and 5,
# the output should be 15.

def multip(a, b):
    return a*b
print('The result of the multiplication is:', multip(3, 5))

#Homework 6 about Functions: Write a function that receives three parameters: name, weight, and height.
# The default value for name is James. The function calculates the BMI. BMI is: weight/(height^2).
# Weight should be in kg and height should be in meters. For instance, if the weight is 60 kg and the
# height is 1.7 m, then the BMI should be 20.76. The function should return "John's BMI is greater
# than or equal to 22" if the MBI is greater than or equal to 22. Otherwise, the function should
# return "John's BMI is less than 22". That is if the name is John. The name could be anything.
# Call the function and print its output.
def BMI_cal(weight, height, name = 'James', ):
    bmi = weight / height**2
    if bmi >= 22:
        return name + "'s BMI is greater than or equal to 22"
    else:
        return name + "'s BMI is less than 22"
output = BMI_cal(name = 'John', weight = 60, height = 1.7)
print(output)

#Homework 7 about Integers and Floats: Write a program that receives an integer, greater than or equal
# to 2, from the user and prints whether that number is odd or even.
num = input('Please enter an integer: ')
num = int(num) # Python takes all user inputs to be of type string. We have to manually cast them to int if needed.
if num % 2 == 0:
    print('even')
else:
    print('odd')


#Homework 8 about Integers and Floats: The Fibonacci Sequence is a series of numbers. The first two numbers
# are 0 and 1. The next number is found by adding up the two numbers before it.
# For example, 0, 1, 1, 2, 3, 5, 8, 13, 21. The next number in this series is 13+21 = 34. Write a program
# that receives an integer from the user, called n, and prints out Fibonacci series up to n terms. For example,
# if the user types 5, your program should print out 0, 1, 1, 2, 3. If the user types 11, your program should
# print out 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55.
n = int(input('Please enter an integer:'))
i = 0
j = 1
print(i)
print(j)
for iterator in range(n-2):
    fib = i + j
    print(fib)
    i = j
    j = fib


# Only 1 session
#Homework 9 about Integers and Floats: Write a program that receives an integer from the user, called n,
# and prints the first n prime numbers. For example, if the input is 7, the output should
# be: 2, 3, 5, 7, 11, 13, 17.
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

#Homework 10 about Strings: Write a function to return a string made of the first 2 and the last 2 chars
# from a given string. If the string length is 4 or less, return the entire string. For instance, it should
# return unrn for unicorn and it should return abc for abc. Call that function and print its output.
def string_both_ends(str):
  if len(str) <= 4:
    return str
  return str[0:2] + str[-2:]

print(string_both_ends('w3resource'))
print(string_both_ends('w3'))
print(string_both_ends('w'))

#Homework 11 about Strings: Write a python program to get a string as input from the user and print the
# third character from the end. For instance, it should print o for unicorn.
name = input('Please enter a word: ')
print(name[-3])

# Homework 12 about Lists, Tuples, and Sets: Write a function that receives a tuple as input. The tuple
# might include duplicates. Convert the tuple to a set which will remove duplicates automatically. Then
# convert the set to a list. Then sort the list. Then create a new list that includes the items in the
# previous list, each one duplicated as many times as its index. For instance, the first item in the list
# would appear only once in the new list, the second item in the list would appear two times in the list, etc.
# Then it returns the new list. For instance, if the input is ('b', 'a', 'c', 'a', 'c'), the output should
# be ['a', 'b', 'b', 'c', 'c', 'c']. If the input is (8, 5, 6, 6), the output should be [5, 6, 6, 8, 8, 8].
def list_to_list(tpl):
  set1 = set(tpl)
  list1 = list(set1)
  list1.sort()
  list2 = []
  for indx, item in enumerate(list1):
      for i in range(indx + 1):
          list2.append(item)
  return list2

list_to_list((8, 5, 6, 6))
list_to_list(('b', 'a', 'c', 'a', 'c'))
set_to_list(('hi', 'yy', 'you'))

# Homework 13 about Lists, Tuples, and Sets: Write a function that receives a list of integers as its
# argument. The function should join individual elements of this list of integers to create a string.
# Inside the string, the elements should be separated using a comma. Then return the string. For instance,
# if you call the function and pass [1, 2, 3], the returned string should be "1,2,3". Please note that there
# is no space around the comma in the string. Please note that the join function only operates on
# lists whose elements are string. Since your list includes integers in this case, you need to take an
# extra step to make it possible to use the join function.
def join2(lst):
    lst_str = []
    for i in lst:
        lst_str.append(str(i))
    return ','.join(lst_str)
print(join2([1, 2, 3]))

#Homework 14 about Lists, Tuples, and Sets: Write a function that receives a list of integers and returns
# that list after removing prime numbers from the list. The number one is not a prime number. Test your
# function with multiple lists of numbers and make sure it works properly. For instance, if the input
# is [1, 2, 3, 4, 5, 6, 7], it should return [1, 4, 6].
def is_prime(num):
    for x in range(2, num):
        if num%x == 0:
            return False
    return True
def remove_prime(nums):
    lis_new = []
    for num in nums:
        if not is_prime(num):
            lis_new.append(num)
    return lis_new
lis = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(remove_prime(lis))

# Homework 15 about Dictionaries: Write a function called func_dict(list1, list2) that receives two lists of the same
# length as its arguments, creates a dictionary called dict whose keys are items from list_1 and whose values are items
# from list_2, and returns the dict. For instance, if list_1 = ['Ten', 'Twenty', 'Thirty'] and list_2 = [10, 20, 30],
# then your function should return {'Ten': 10, 'Twenty': 20, 'Thirty': 30}.
def func_dict(list1, list2):
    dict = {}
    for i in range(len(list1)):
        key = list1[i]
        value = list2[i]
        dict[key] = value
    return dict
print(func_dict(list1 = ['Ten', 'Twenty', 'Thirty'], list2 = [10, 20, 30]))

#Homework 16 about Dictionaries: Write a function that receives a dictionary and a variable as its arguments and
# returns True if that variable exists among the values of the dictionary and False if it does not.
# For instance, if dict={'name': 'John', 'expertise': 'Math'} and variable='John', then your function should return True.
# If dict={'name': 'John', 'expertise': 'Math'} and variable='name', then your function should return False.
def value_exists(dict, var):
    if var in dict.values():
        return 'True'
    else:
        return 'False'

#Homework 17 about Dictionaries: Write a function that receives a dictionary as input and returns the key
# for the minimum value among the dictionary values. Call that function and print its output. You can test
# your function with {'Math': 25, 'History': 20, 'Physics': 18, 'Geography': 19} and it should return Physics.
def min_dict(dict):
    min_value = min(dict.values())
    for key, value in dict.items():
        if value == min_value:
            return key
print(min_dict({'Math': 25, 'History': 20, 'Physics': 18, 'Geography': 19}))

# Source: https://pynative.com/python-numpy-exercise/
# Homework 18 about Libraries: NumPy stands for Numerical Python. This Python library provides support for
# large multidimensional array objects and various tools to work with them. The difference between Python
# lists and NumPy arrays: Lists contain elements with different data types, but NumPy arrays contain only
# homogeneous elements, i.e. elements having the same data type. This makes it more efficient at storing
# and manipulating the array. This difference becomes apparent when the array has a large number of elements,
# say thousands or millions. Also, with NumPy arrays, you can perform element-wise operations, something
# which is not possible using Python lists! This is the reason why NumPy arrays are preferred over Python
# lists when performing mathematical operations on a large amount of data. Write a program to delete the
# second column from the following array and insert the following new column in its place, and print the result.
# original_array = numpy.array(
# [[34 43 73]
# [82 22 12]
# [53 94 66]])
# new_column = numpy.array([[10,10,10]])
# After insertion, your array should look like:
# [[34 10 73]
# [82 10 12]
# [53 10 66]]
import numpy

print("Printing Original array")
original_array = numpy.array([[34, 43, 73], [82, 22, 12], [53, 94, 66]])
print(original_array)

print("Array after deleting column 2 on axis 1")
after_deletion_array = numpy.delete(original_array , 1, axis=1)
print(after_deletion_array)

print("Array after inserting column 2 on axis 1")
new_column = numpy.array([[10, 10, 10]])
after_insertion_array = numpy.insert(after_deletion_array, 1, new_column, axis=1)
print (after_insertion_array)

# Source: https://pynative.com/python-pandas-exercise/
#Homework 19 about Libraries: Pandas is a Python library for data manipulation and analysis. Download this CSV
# file and take a look at it. Use pandas library to read this file as a data frame. Write a program to find
# the name of the company that has the most expensive car. Print out the name of this company. The correct
# output is mercedes-benz.
import pandas as pd
df = pd.read_csv("I:/Personal/Website/Data/Automobile_data.csv")
max_price = df['price'].max() # Returns the maximum value in the price column.
indexmax = df['price'].idxmax() # Returns the index of the row with the first incident of the maximum value.
company = df.loc[indexmax, 'company'] # Get the content of one cell as a single value.
print(company)


#Homework 20 about reading writing txt files: Prepare a txt file that has five lines with three words on each line,
# separated with a space. Write a program that reads the txt file and makes three lists out of it and prints
# the three lists. The elements of the first list are the first word on each line. The elements of the second
# list are the second word on each line. The elements of the third list are the third word on each line. Each
# list has five elements. Make sure that there are no new line characters in the elements.
with open('I:/Teaching/Intro to Comp Prog IT 109/file.txt', 'r') as f:
    list1 = []
    list2 = []
    list3 = []
    for line in f:
        line = line.rstrip('\n') # It will remove the \n from the end of the line.
        split_list = line.split(' ')
        list1.append(split_list[0])
        list2.append(split_list[1])
        list3.append(split_list[2])
print(list1)
print(list2)
print(list3)


#Homework 21 about reading writing txt files: Make a txt file and write 10 lines of text in it, anything. Read
# the file in Python and write a new txt file using your code that includes every other line in the first
# text file. Therefore, the new txt file has five lines which are line 1, line 3, line 5, line 7, and line 9 in
# the first txt file.
with open('I:/Teaching/Intro to Comp Prog IT 109/file.txt', 'r') as r_f:
    with open('I:/Teaching/Intro to Comp Prog IT 109/new_file.txt', 'w') as w_f:
        for l in r_f:
            w_f.write(l)
            r_f.readline() # Moves the location one line forward


# Homework 22 about Problem Solving:
# Introduction: A magic square is a 2D matrix composed of n^2 integers where n is the length of one row or column.
# In a magic square each row, each column, and the two diagonals must sum to the same value.
# Problem: Given a 2D matrix, your program must determine if the square is magic or not magic. It will print
# "True" or "False" accordingly.
# Input: Your program will first take an input n, representing the length of one row of the matrix from the user.
# It will then take n lines of input containing n integers separated by spaces from the user.
'''Sample Input:
3
2 2 2
2 2 2
2 2 2
Output: "True"

Input:
3
2 7 6
9 5 1
4 3 8
Output: "True"

Input:
4
16 2 3 13
5 11 10 8
9 7 6 12
4 14 15 1
Output: "True"

Input:
4
12 3 4 5
5 67 8 9
102 3 4 6
34 2 89 0
Output: "False"
'''

#Input
n = int(input("Enter the size of the square matrix: "))
matrix = [] # This will be a 2D list
for rows in range(n):
    nums = input("Enter the rows one at a time and use space to separate the numbers: ")
    matrix.append([int(x) for x in nums.split(' ')]) # Each row of numbers will be converted to a list and appended to the 2D list

magic = True
target = sum(matrix[0]) # The summation of the first row

sum_of_primary_diagonal = 0
sum_of_secondary_diagonal = 0
for i in range(n):
    sum_of_primary_diagonal += matrix[i][i] # Find the sum of the primary diagonal
    sum_of_secondary_diagonal += matrix[n - 1 - i][i]  # Find the sum of the secondary diagonal

    if sum(matrix[i]) != target: # Check if the sum of each row is the same as target
        magic = False
        break

    sum_column = 0
    for j in range(n):
        sum_column += matrix[j][i] # Find the sum of each column
    if sum_column != target: # Check if the sum of each column is the same as target
        magic=False
        break

if sum_of_primary_diagonal != target or sum_of_secondary_diagonal != target:
    magic = False

print(magic)


