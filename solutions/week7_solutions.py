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

def list_to_list(tpl):
    unique_sorted = sorted(set(tpl))
    out = []
    for idx, item in enumerate(unique_sorted, start=1):
        out.extend([item] * idx)
    return out

print(list_to_list((8, 5, 6, 6)))                 # [5, 6, 6, 8, 8, 8]
print(list_to_list(('b', 'a', 'c', 'a', 'c')))     # ['a', 'b', 'b', 'c', 'c', 'c']
print(list_to_list(('hi', 'yy', 'you')))           # ['hi', 'yy', 'yy', 'you', 'you', 'you']


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

def join2(lst):
    return ','.join(str(x) for x in lst)

print(join2([1, 2, 3]))  # "1,2,3"


# %%
'''
Homework 3 about Lists, Tuples, and Sets: Write a function that receives a tuple of integers
and returns a new tuple containing only the even numbers from it.
For example, if the input is (1, 2, 3, 4, 5, 6), the output should be (2, 4, 6).
'''

def even_numbers_from_tuple(nums):
    return tuple(x for x in nums if x % 2 == 0)

# Test cases
print(even_numbers_from_tuple((1, 2, 3, 4, 5, 6)))   # (2, 4, 6)
print(even_numbers_from_tuple((7, 9, 11)))          # ()
print(even_numbers_from_tuple((10, 20, 30)))        # (10, 20, 30)


# %%
'''
Homework 4 about Lists, Tuples, and Sets: Write a function to flatten a list by one nesting level.
It should take a list whose elements may include lists/tuples/sets and return a single flat list.
Example: [1, [2, 3], (4, 5), {6, 7}] -> [1, 2, 3, 4, 5, 6, 7].
'''

def flatten_one_level(seq):
    out = []
    for x in seq:
        if isinstance(x, (list, tuple, set)):
            # For sets, convert to a deterministic order
            iterable = list(x) if not isinstance(x, set) else sorted(x)
            out.extend(iterable)
        else:
            out.append(x)
    return out

print(flatten_one_level([1, [2, 3], (4, 5), {6, 7}]))


# %%
'''
Homework 5 about Lists, Tuples, and Sets: Given a tuple t, return a new tuple in which the first occurrence
of the minimum value and the first occurrence of the maximum value are swapped. All other elements remain
in their original positions. Example: (3, 1, 4, 1, 5) -> (3, 5, 4, 1, 1).
'''

def swap_min_max_in_tuple(t):
    if not t:
        return t
    mn, mx = min(t), max(t)
    if mn == mx:
        return t
    t_list = list(t)
    i_min = t_list.index(mn)
    i_max = t_list.index(mx)
    t_list[i_min], t_list[i_max] = t_list[i_max], t_list[i_min]
    return tuple(t_list)

print(swap_min_max_in_tuple((3, 1, 4, 1, 5)))
print(swap_min_max_in_tuple((9, 9, 9)))


# %%
'''
Homework 6 about Lists, Tuples, and Sets: Write a function that takes two lists and returns:
(1) the sorted list of unique elements in their intersection, and
(2) the sorted list of unique elements in their symmetric difference.
Use set operations, then convert to lists and sort before returning.
'''

def intersection_and_symdiff(a, b):
    sa, sb = set(a), set(b)
    inter = sorted(sa & sb)
    symd  = sorted(sa ^ sb)
    return inter, symd

print(intersection_and_symdiff([1,2,3,4], [3,4,5,6]))   # ([3,4], [1,2,5,6])


# %%
'''
Homework 7 about Lists, Tuples, and Sets: Remove duplicates from a list while preserving the order
of first occurrence. Return the deduplicated list. Example: [3,1,3,2,1] -> [3,1,2].
'''

def dedup_preserve_order(lst):
    seen = set()
    out = []
    for x in lst:
        if x not in seen:
            seen.add(x)
            out.append(x)
    return out

print(dedup_preserve_order([3, 1, 3, 2, 1, 2, 4, 4]))


# %%
'''
Homework 8 about Lists, Tuples, and Sets: Compute the moving average of a list of numbers given a window size k.
Return a list of floats of length len(nums) - k + 1 where each element is the average of a window.
Raise ValueError if k <= 0 or k > len(nums).
'''

def moving_average(nums, k):
    if k <= 0 or k > len(nums):
        raise ValueError("Invalid window size k")
    window_sum = sum(nums[:k])
    out = [window_sum / k]
    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]
        out.append(window_sum / k)
    return out

print(moving_average([1,2,3,4,5,6], 3))  # [2.0, 3.0, 4.0, 5.0]


# %%
'''
Homework 9 about Lists, Tuples, and Sets: Given a list, return a list of (item, count) tuples sorted by
descending count then ascending item. Use Counter from collections for counting.
'''

from collections import Counter

def frequency_sorted(lst):
    cnt = Counter(lst)
    return sorted(cnt.items(), key=lambda kv: (-kv[1], kv[0]))

print(frequency_sorted(['a','b','a','c','b','a','d']))


# %%
'''
Homework 10 about Lists, Tuples, and Sets: Given a list of (name, score) pairs, normalize scores to the [0, 1]
range using (x - min) / (max - min). If all scores are equal, return 0.0 for all. Return a new list of tuples.
Example: [("Ann", 50), ("Bob", 80), ("Cia", 80)] -> [("Ann", 0.0), ("Bob", 1.0), ("Cia", 1.0)].
'''

def normalize_scores(pairs):
    if not pairs:
        return []
    scores = [s for _, s in pairs]
    mn, mx = min(scores), max(scores)
    if mx == mn:
        return [(n, 0.0) for n, _ in pairs]
    return [(n, (s - mn) / (mx - mn)) for n, s in pairs]

print(normalize_scores([("Ann", 50), ("Bob", 80), ("Cia", 80)]))