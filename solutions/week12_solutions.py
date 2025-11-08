# %%
# Homework 1 about Problem Solving:
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



# %%
