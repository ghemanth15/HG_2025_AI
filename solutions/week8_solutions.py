# %%
'''
Homework 1 about Lists, Tuples, and Sets: Write a function that receives a list of integers and returns
that list after removing prime numbers from the list. The number one is not a prime number. Test your
function with multiple lists of numbers and make sure it works properly. For instance, if the input
is [1, 2, 3, 4, 5, 6, 7], it should return [1, 4, 6].
'''

def is_prime(num):
    for x in range(2, num):
        if num % x == 0:
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

# %%
'''
Homework 2 about Lists, Tuples, and Sets: Write a function that receives a tuple of integers
and returns the maximum and minimum values as a tuple (max, min).
For example, if the input is (4, 7, 2, 9, 1), the output should be (9, 1).
'''

def max_min_tuple(nums):
    return (max(nums), min(nums))

print(max_min_tuple((4, 7, 2, 9, 1)))   # (9, 1)


# %%
'''
Homework 3 about Lists, Tuples, and Sets: Write a function that receives two sets of integers
and returns their union, intersection, and difference as a tuple of three sets.
For example, if set1 = {1, 2, 3} and set2 = {2, 3, 4}, the output should be
({1, 2, 3, 4}, {2, 3}, {1}).
'''

def set_operations(set1, set2):
    return (set1 | set2, set1 & set2, set1 - set2)

print(set_operations({1, 2, 3}, {2, 3, 4}))


# %%
'''
Homework 4 about Lists, Tuples, and Sets: Write a function that receives a list of strings
and returns a new list with all duplicates removed, while preserving the order of first appearance.
For example, if the input is ["apple", "banana", "apple", "cherry"], the output should be
["apple", "banana", "cherry"].
'''

def remove_duplicates(strings):
    seen = set()
    result = []
    for s in strings:
        if s not in seen:
            result.append(s)
            seen.add(s)
    return result

print(remove_duplicates(["apple", "banana", "apple", "cherry"]))



# %%
'''
Homework 5 about Lists, Tuples, and Sets: Write a function that receives a list of integers
and returns a tuple (even_count, odd_count) representing how many even and odd numbers are in the list.
For example, if the input is [1, 2, 3, 4, 5, 6], the output should be (3, 3).
'''

def count_even_odd(nums):
    even = sum(1 for n in nums if n % 2 == 0)
    odd = len(nums) - even
    return (even, odd)

print(count_even_odd([1, 2, 3, 4, 5, 6]))


# %%
'''
Homework 6 about Dictionaries: Write a function called func_dict(list1, list2) that receives two lists of the same
length as its arguments, creates a dictionary called dict whose keys are items from list_1 and whose values are items
from list_2, and returns the dict. For instance, if list_1 = ['Ten', 'Twenty', 'Thirty'] and list_2 = [10, 20, 30],
then your function should return {'Ten': 10, 'Twenty': 20, 'Thirty': 30}.
'''

def func_dict(list1, list2):
    dict = {}
    for i in range(len(list1)):
        key = list1[i]
        value = list2[i]
        dict[key] = value
    return dict

print(func_dict(list1=['Ten', 'Twenty', 'Thirty'], list2=[10, 20, 30]))


# %%
'''
Homework 7 about Dictionaries: Write a function that receives a dictionary of student names as keys
and their scores as values, and returns the name of the student with the highest score.
For example, if the input is {'Alice': 85, 'Bob': 92, 'Charlie': 78}, the output should be 'Bob'.
'''

def top_student(scores):
    return max(scores, key=scores.get)

print(top_student({'Alice': 85, 'Bob': 92, 'Charlie': 78}))


# %%
'''
Homework 8 about Dictionaries: Write a function that receives a string and returns a dictionary
where the keys are the characters of the string and the values are the number of times each character appears.
For example, if the input is "banana", the output should be {'b': 1, 'a': 3, 'n': 2}.
'''

def char_frequency(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    return freq

print(char_frequency("banana"))


# %%
'''
Homework 9 about Dictionaries: Write a function that receives a dictionary with items and prices,
and returns the total price of all items.
For example, if the input is {'apple': 2.5, 'banana': 1.2, 'milk': 3.0}, the output should be 6.7.
'''

def total_price(items):
    return sum(items.values())

print(total_price({'apple': 2.5, 'banana': 1.2, 'milk': 3.0}))


# %%
'''
Homework 10 about Dictionaries: Write a function that receives two dictionaries and merges them into
one dictionary. If a key exists in both, the value from the second dictionary should be used.
For example, if dict1 = {'a': 1, 'b': 2} and dict2 = {'b': 3, 'c': 4},
the output should be {'a': 1, 'b': 3, 'c': 4}.
'''

def merge_dicts(d1, d2):
    merged = d1.copy()
    merged.update(d2)
    return merged

print(merge_dicts({'a': 1, 'b': 2}, {'b': 3, 'c': 4}))