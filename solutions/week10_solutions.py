# %%
'''
Extract 'make' and 'price' columns from the full automobile CSV file.
Clean the data by removing rows with missing price ('?').
Convert price to numeric and save the cleaned output to a new CSV file.
'''

import pandas as pd
# Step 1: Load full CSV file
df = pd.read_csv("Automobile_data.csv")  # replace with actual path if needed
# Step 2: Extract only 'make' and 'price' columns
df_make_price = df[['make', 'price']]
# Step 3: Filter out rows with missing price
df_make_price = df_make_price[df_make_price['price'] != '?']
# Step 4: Convert price to numeric
df_make_price['price'] = pd.to_numeric(df_make_price['price'])
# Step 5: Save new CSV file
df_make_price.to_csv("make_price_cleaned.csv", index=False)
print("new CSV saved as 'make_price_cleaned.csv'")

# %%
'''
Homework 0 about Libraries: NumPy stands for Numerical Python. This Python library provides support for
large multidimensional array objects and various tools to work with them. The difference between Python
lists and NumPy arrays: Lists contain elements with different data types, but NumPy arrays contain only
homogeneous elements, i.e. elements having the same data type. This makes it more efficient at storing
and manipulating the array. This difference becomes apparent when the array has a large number of elements,
say thousands or millions. Also, with NumPy arrays, you can perform element-wise operations, something
which is not possible using Python lists! This is the reason why NumPy arrays are preferred over Python
lists when performing mathematical operations on a large amount of data. Write a program to delete the
second column from the following array and insert the following new column in its place, and print the result.
original_array = numpy.array(
[[34 43 73]
[82 22 12]
[53 94 66]])
new_column = numpy.array([[10,10,10]])
After insertion, your array should look like:
[[34 10 73]
[82 10 12]
[53 10 66]]
'''
import numpy

print("Printing Original array")
original_array = numpy.array([[34, 43, 73],
                              [82, 22, 12],
                              [53, 94, 66]])
print(original_array)

print("Array after deleting column 2 on axis 1")
after_deletion_array = numpy.delete(original_array, 1, axis=1)
print(after_deletion_array)

print("Array after inserting column 2 on axis 1")
new_column = numpy.array([[10, 10, 10]]).T  # column vector
after_insertion_array = numpy.insert(after_deletion_array, 1, new_column, axis=1)
print(after_insertion_array)

# %%
'''
Homework 1 about Libraries: Pandas is a Python library for data manipulation and analysis. 
Download this CSV file and take a look at it. Use pandas library to read this file as a data frame. 
Write a program to find the name of the company that has the most expensive car. 
Print out the name of this company. The correct output is mercedes-benz.
'''

import pandas as pd
df = pd.read_csv("make_price_cleaned.csv")
max_price = df['price'].max()
indexmax = df['price'].idxmax()
company = df.loc[indexmax, 'make']
print(company)


# %%
'''
Homework 2 about Libraries: Use the math library to compute the greatest common divisor (GCD) 
of two integers input by the user.
'''

import math

a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))
print("GCD:", math.gcd(a, b))


# %%
'''
Homework 3 about Libraries: Use the random library to generate a random password of length 10. 
The password should contain uppercase letters, lowercase letters, digits, and symbols.
'''

import random, string

chars = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(chars) for _ in range(10))
print("Random password:", password)


# %%
'''
Homework 4 about Libraries: Use numpy to create a 5x5 matrix of random integers between 1 and 50. 
Then compute the row sums and column sums.
'''

import numpy as np

arr = np.random.randint(1, 51, size=(5, 5))
print("Matrix:\n", arr)
print("Row sums:", arr.sum(axis=1))
print("Column sums:", arr.sum(axis=0))


# %%
'''
Homework 5 about Libraries: Use datetime to calculate the number of days between 
two given dates: July 4, 2020 and September 6, 2025.
'''

from datetime import date

d1 = date(2020, 7, 4)
d2 = date(2025, 9, 6)
print("Days difference:", (d2 - d1).days)


# %%
'''
Homework 6 about Modules: Write a module named "math_utils.py" with a function power(base, exp) 
that returns base raised to exp. Import this module and test it with 2^5.
'''


import utils
print("2^5 =", utils.power(2, 5))


# %%
'''
Homework 7 about Modules: Write a module named "greetings.py" with a function hello(name) 
that prints "Hello, <name>!". Import and test it.
'''

import utils
utils.hello("Aishwarya")


# %%
'''
Homework 8 about Modules: Write a module named "geometry.py" with functions area_rectangle(l, w) 
and perimeter_rectangle(l, w). Import the module and test both functions.
'''

import utils
print("Area:", utils.area_rectangle(4, 6))
print("Perimeter:", utils.perimeter_rectangle(4, 6))


# %%
'''
Homework 9 about Modules: Write a module named "text_utils.py" with a function word_count(s) 
that returns the number of words in a string. Import it and test it.
'''

import utils
print("Word count:", utils.word_count("Modules and Libraries in Python"))


# %%
'''
Homework 10 about Modules: Write a module named "stats_utils.py" with a function median(lst) 
that returns the median of a list of numbers without using statistics library. 
Import and test it with [7, 1, 3, 5].
'''

import utils
print("Median:", utils.median([7, 1, 3, 5]))
# %%
