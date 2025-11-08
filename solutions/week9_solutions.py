# %%
'''
Homework 1 about Dictionaries: Write a function that receives a dictionary and a variable as its arguments and
returns True if that variable exists among the values of the dictionary and False if it does not.
For instance, if dict={'name': 'John', 'expertise': 'Math'} and variable='John', then your function should return True.
If dict={'name': 'John', 'expertise': 'Math'} and variable='name', then your function should return False.
'''

def value_exists(d, var):
    return var in d.values()

print(value_exists({'name': 'John', 'expertise': 'Math'}, 'John'))  # True
print(value_exists({'name': 'John', 'expertise': 'Math'}, 'name'))  # False

# %%
'''
Homework 2 about Dictionaries: Write a function that receives a dictionary as input and returns the key
for the minimum value among the dictionary values. Call that function and print its output. You can test
your function with {'Math': 25, 'History': 20, 'Physics': 18, 'Geography': 19} and it should return Physics.
'''

def min_dict(d):
    return min(d, key=d.get)

print(min_dict({'Math': 25, 'History': 20, 'Physics': 18, 'Geography': 19}))  # Physics


# %%
'''
Homework 3 about Dictionaries: Write a function that receives a dictionary of student names as keys and their scores
as values, and returns the average score of the class. For example, if the input is {'Alice': 80, 'Bob': 90, 'Charlie': 70},
the output should be 80.0.
'''

def average_score(scores):
    return sum(scores.values()) / len(scores) if scores else 0

print(average_score({'Alice': 80, 'Bob': 90, 'Charlie': 70}))  # 80.0


# %%
'''
Homework 4 about Dictionaries: Write a function that receives a dictionary and returns a new dictionary with
the keys and values swapped. For example, if the input is {'a': 1, 'b': 2, 'c': 3}, the output should be {1: 'a', 2: 'b', 3: 'c'}.
'''

def swap_dict(d):
    return {v: k for k, v in d.items()}

print(swap_dict({'a': 1, 'b': 2, 'c': 3}))  # {1: 'a', 2: 'b', 3: 'c'}


# %%
'''
Homework 5 about Dictionaries: Write a function that receives a dictionary and a key as input,
and removes that key-value pair from the dictionary if it exists. Return the updated dictionary.
For example, if the input is {'x': 10, 'y': 20, 'z': 30} and key='y', the output should be {'x': 10, 'z': 30}.
'''

def remove_key(d, key):
    if key in d:
        del d[key]
    return d

print(remove_key({'x': 10, 'y': 20, 'z': 30}, 'y'))  # {'x': 10, 'z': 30}

# %%
'''
Homework 6 about Dictionaries: Write a function that receives two dictionaries and merges them into one.
If the same key exists in both, the value from the second dictionary should overwrite the first.
For example, if dict1 = {'a': 1, 'b': 2} and dict2 = {'b': 3, 'c': 4}, the output should be {'a': 1, 'b': 3, 'c': 4}.
'''

def merge_dicts(d1, d2):
    merged = d1.copy()
    merged.update(d2)
    return merged

print(merge_dicts({'a': 1, 'b': 2}, {'b': 3, 'c': 4}))  # {'a': 1, 'b': 3, 'c': 4}


# %%
'''
Homework 7 about Dictionaries: Write a function that receives a string and returns a dictionary
where each key is a word and its value is the number of times that word appears in the string.
For example, if the input is "apple banana apple orange banana", the output should be
{'apple': 2, 'banana': 2, 'orange': 1}.
'''

def word_count(s):
    words = s.split()
    freq = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1
    return freq

print(word_count("apple banana apple orange banana"))  # {'apple': 2, 'banana': 2, 'orange': 1}

# %%
'''
Homework 8 about Dictionaries: Write a function that receives a dictionary of items and their prices,
and returns the item with the highest price. For example, if the input is {'apple': 2.5, 'banana': 1.2, 'milk': 3.0},
the output should be 'milk'.
'''

def most_expensive_item(d):
    return max(d, key=d.get)

print(most_expensive_item({'apple': 2.5, 'banana': 1.2, 'milk': 3.0}))  # milk

# %%
'''
Homework 9 about Dictionaries: Write a function that receives a dictionary of numbers as keys and their squares as values,
and returns True if all values are correct squares of the keys, otherwise returns False.
For example, if the input is {2: 4, 3: 9, 4: 16}, the output should be True. If the input is {2: 5, 3: 9}, the output should be False.
'''

def check_squares(d):
    for k, v in d.items():
        if k * k != v:
            return False
    return True

print(check_squares({2: 4, 3: 9, 4: 16}))  # True
print(check_squares({2: 5, 3: 9}))         # False

# %%
'''
Homework 10 about Dictionaries: Write a function that receives a dictionary where the values are lists of integers,
and returns a dictionary with the same keys but where each list is replaced by its maximum value.
For example, if the input is {'a': [1, 2, 3], 'b': [5, 0], 'c': [10]}, the output should be {'a': 3, 'b': 5, 'c': 10}.
'''

def max_in_lists(d):
    return {k: max(v) for k, v in d.items()}

print(max_in_lists({'a': [1, 2, 3], 'b': [5, 0], 'c': [10]}))  # {'a': 3, 'b': 5, 'c': 10}
