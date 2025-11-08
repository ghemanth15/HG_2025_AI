# %%
'''
Homework 1 about Lists, Tuples, and Sets: Write a function that receives a tuple as input. The tuple
might include duplicates. Convert the tuple to a set which will remove duplicates automatically. Then
convert the set to a list. Then sort the list. Then create a new list that includes the items in the
previous list, each one duplicated as many times as its index. For instance, the first item in the list
would appear only once in the new list, the second item in the list would appear two times in the list, etc.
Then it returns the new list. For instance, if the input is ('b', 'a', 'c', 'a', 'c'), the output should
be ['a', 'b', 'b', 'c', 'c', 'c']. If the input is (8, 5, 6, 6), the output should be [5, 6, 6, 8, 8, 8].
'''


# %%
'''
Homework 2 about Lists, Tuples, and Sets: Write a function that receives a list of integers as its
argument. The function should join individual elements of this list of integers to create a string.
Inside the string, the elements should be separated using a comma. Then return the string. For instance,
if you call the function and pass [1, 2, 3], the returned string should be "1,2,3". Please note that there
is no space around the comma in the string. Please note that the join function only operates on
lists whose elements are string. Since your list includes integers in this case, you need to take an
extra step to make it possible to use the join function.
'''


# %%
'''
Homework 3 about Lists, Tuples, and Sets: Write a function that receives a tuple of integers
and returns a new tuple containing only the even numbers from it.
For example, if the input is (1, 2, 3, 4, 5, 6), the output should be (2, 4, 6).
'''




# %%
'''
Homework 4 about Lists, Tuples, and Sets: Write a function to flatten a list by one nesting level.
It should take a list whose elements may include lists/tuples/sets and return a single flat list.
Example: [1, [2, 3], (4, 5), {6, 7}] -> [1, 2, 3, 4, 5, 6, 7].
'''

# %%
'''
Homework 5 about Lists, Tuples, and Sets: Given a tuple t, return a new tuple in which the first occurrence
of the minimum value and the first occurrence of the maximum value are swapped. All other elements remain
in their original positions. Example: (3, 1, 4, 1, 5) -> (3, 5, 4, 1, 1).
'''


# %%
'''
Homework 6 about Lists, Tuples, and Sets: Write a function that takes two lists and returns:
(1) the sorted list of unique elements in their intersection, and
(2) the sorted list of unique elements in their symmetric difference.
Use set operations, then convert to lists and sort before returning.
'''



# %%
'''
Homework 7 about Lists, Tuples, and Sets: Remove duplicates from a list while preserving the order
of first occurrence. Return the deduplicated list. Example: [3,1,3,2,1] -> [3,1,2].
'''



# %%
'''
Homework 8 about Lists, Tuples, and Sets: Compute the moving average of a list of numbers given a window size k.
Return a list of floats of length len(nums) - k + 1 where each element is the average of a window.
Raise ValueError if k <= 0 or k > len(nums).
'''



# %%
'''
Homework 9 about Lists, Tuples, and Sets: Given a list, return a list of (item, count) tuples sorted by
descending count then ascending item. Use Counter from collections for counting.
'''



# %%
'''
Homework 10 about Lists, Tuples, and Sets: Given a list of (name, score) pairs, normalize scores to the [0, 1]
range using (x - min) / (max - min). If all scores are equal, return 0.0 for all. Return a new list of tuples.
Example: [("Ann", 50), ("Bob", 80), ("Cia", 80)] -> [("Ann", 0.0), ("Bob", 1.0), ("Cia", 1.0)].
'''

