# %%
'''
Homework 1 about Strings: Write a function to return a string made of the first 2 and the last 2 chars
from a given string. If the string length is 4 or less, return the entire string. For instance, it should
return unrn for unicorn and it should return abc for abc. Call that function and print its output.
'''

def string_both_ends(s):
    if len(s) <= 4:
        return s
    return s[0:2] + s[-2:]

print(string_both_ends('w3resource'))
print(string_both_ends('w3'))
print(string_both_ends('w'))


# %%
'''
Homework 2 about Strings: Write a python program to get a string as input from the user and print the
third character from the end. For instance, it should print 'o' for unicorn.
'''

name = input('Please enter a word: ')
if len(name) >= 3:
    print(name[-3])
else:
    print("The word is too short.")


# %%
'''
Homework 3 about Strings: Write a function that counts how many vowels are in a given string.
The function should be case-insensitive. Call the function with at least two examples.
'''

def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for ch in s if ch in vowels)

print("Vowel count in 'unicorn':", count_vowels("unicorn"))
print("Vowel count in 'GRADUATE':", count_vowels("GRADUATE"))


# %%
'''
Homework 4 about Strings: Write a program that receives a string from the user and prints whether
it is a palindrome or not (ignoring spaces and case).
'''

s = input("Enter a string: ")
cleaned = s.replace(" ", "").lower()
if cleaned == cleaned[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")


# %%
'''
Homework 5 about Strings: Write a function that takes two strings and returns True if one string
is an anagram of the other (ignoring spaces and case). Otherwise, return False.
'''

def is_anagram(s1, s2):
    return sorted(s1.replace(" ", "").lower()) == sorted(s2.replace(" ", "").lower())

print(is_anagram("listen", "silent"))
print(is_anagram("hello", "world"))


# %%
'''
Homework 6 about Strings: Write a program that receives a sentence from the user and counts the
number of words in it. Assume words are separated by spaces.
'''

sentence = input("Enter a sentence: ")
words = sentence.split()
print("Word count:", len(words))


# %%
'''
Homework 7 about Strings: Write a function that replaces all vowels in a string with the character '*'.
Call the function with a few examples.
'''

def mask_vowels(s):
    vowels = "aeiouAEIOU"
    return ''.join('*' if ch in vowels else ch for ch in s)

print(mask_vowels("unicorn"))
print(mask_vowels("Graduate Level"))


# %%
'''
Homework 8 about Strings: Write a program that receives a string and prints the frequency of each character
in the string. Ignore case and spaces.
'''

s = input("Enter a string: ")
freq = {}
for ch in s.lower():
    if ch.isalpha():
        freq[ch] = freq.get(ch, 0) + 1

print("Character frequencies:")
for k, v in freq.items():
    print(k, ":", v)


# %%
'''
Homework 9 about Strings: Write a program that receives a string and prints all unique characters in it
(sorted alphabetically). For example, "banana" should output 'abn'.
'''

s = input("Enter a string: ")
unique_chars = sorted(set(s))
print("".join(unique_chars))


# %%
'''
Homework 10 about Strings: Write a program that receives a string and checks if it contains at least
one digit, one uppercase letter, and one lowercase letter. Print "Valid string" if all conditions are met,
otherwise print "Invalid string".
'''

s = input("Enter a string: ")
has_digit = any(ch.isdigit() for ch in s)
has_upper = any(ch.isupper() for ch in s)
has_lower = any(ch.islower() for ch in s)

if has_digit and has_upper and has_lower:
    print("Valid string")
else:
    print("Invalid string")