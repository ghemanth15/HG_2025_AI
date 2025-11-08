# %%
'''
Prepare sample data files for Reading/Writing TXT file homeworks.
This will create:
- file.txt
- new_file.txt (empty initially, gets written by Homework 2)
- text_input.txt
- file_a.txt
- file_b.txt
- big.txt
'''

# file.txt → 5 lines, 3 words each
with open("Test_Files/file.txt", "w", encoding="utf-8") as f:
    f.write("apple red sweet\n")
    f.write("banana yellow ripe\n")
    f.write("grape purple small\n")
    f.write("mango orange juicy\n")
    f.write("melon green fresh\n")

# text_input.txt → 10+ lines of text
with open("Test_Files/text_input.txt", "w", encoding="utf-8") as f:
    f.write("Python is fun.\n")
    f.write("I like learning Python.\n")
    f.write("Files are easy to read and write.\n")
    f.write("Text processing is powerful.\n")
    f.write("Python is versatile.\n")
    f.write("Data science uses Python a lot.\n")
    f.write("Machine learning is cool.\n")
    f.write("Artificial intelligence is the future.\n")
    f.write("Practice makes perfect.\n")
    f.write("Keep coding every day.\n")

# file_a.txt → 5 lines
with open("Test_Files/file_a.txt", "w", encoding="utf-8") as f:
    f.write("A line 1\n")
    f.write("A line 2\n")
    f.write("A line 3\n")
    f.write("A line 4\n")
    f.write("A line 5\n")

# file_b.txt → 5 lines
with open("Test_Files/file_b.txt", "w", encoding="utf-8") as f:
    f.write("B line 1\n")
    f.write("B line 2\n")
    f.write("B line 3\n")
    f.write("B line 4\n")
    f.write("B line 5\n")

# big.txt → 25 lines
with open("Test_Files/big.txt", "w", encoding="utf-8") as f:
    for i in range(1, 26):
        f.write(f"This is line number {i}\n")

print("Sample files created: file.txt, text_input.txt, file_a.txt, file_b.txt, big.txt")

# %%
'''
Homework 1 about reading/writing txt files:
Prepare a txt file that has five lines with three words on each line, separated with a space.
Write a program that reads the txt file and makes three lists out of it and prints the three lists.
The first list has the first word from each line, the second list has the second word, and the third
list has the third word. Each list has five elements. Make sure there are no newline characters.
'''

list1, list2, list3 = [], [], []
with open('Test_Files/file.txt', 'r', encoding='utf-8') as f:
    for line in f:
        parts = line.strip().split(' ')
        if len(parts) >= 3:
            list1.append(parts[0])
            list2.append(parts[1])
            list3.append(parts[2])

print(list1)
print(list2)
print(list3)


# %%
'''
Homework 2 about reading/writing txt files:
Make a txt file and write 10 lines of text in it (anything). Read the file in Python and write a new
txt file that includes every other line from the first file: lines 1, 3, 5, 7, and 9.
'''

with open('Test_Files/file.txt', 'r', encoding='utf-8') as r_f, \
     open('Test_Files/new_file.txt', 'w', encoding='utf-8') as w_f:
    for idx, line in enumerate(r_f, start=1):
        if idx % 2 == 1:  # odd-numbered lines
            w_f.write(line)


# %%
'''
Homework 3 about reading/writing txt files:
Read a text file and produce a new file "word_freq.txt" that lists each distinct word (case-insensitive)
and its count, sorted by descending count then ascending word. Ignore punctuation next to words.
'''

import re
from collections import Counter

with open('Test_Files/text_input.txt', 'r', encoding='utf-8') as f:
    text = f.read().lower()

words = re.findall(r'\b[\w]+\b', text)
freq = Counter(words)

with open('Test_Files/word_freq.txt', 'w', encoding='utf-8') as out:
    for word, count in sorted(freq.items(), key=lambda kv: (-kv[1], kv[0])):
        out.write(f'{word}\t{count}\n')

print('Created word_freq.txt')


# %%
'''
Homework 4 about reading/writing txt files:
Read a text file and write a new file where each line is prefixed with its 1-based line number
(e.g., "1: <line>"). Save as "numbered_lines.txt".
'''

with open('Test_Files/text_input.txt', 'r', encoding='utf-8') as src, \
     open('Test_Files/numbered_lines.txt', 'w', encoding='utf-8') as dst:
    for i, line in enumerate(src, start=1):
        dst.write(f'{i}: {line}')

print('Created numbered_lines.txt')


# %%
'''
Homework 5 about reading/writing txt files:
Ask the user for a keyword, then read "text_input.txt" and write all lines containing that keyword
(case-insensitive) to "filtered_lines.txt".
'''

keyword = input('Enter keyword to filter: ').lower()
with open('Test_Files/text_input.txt', 'r', encoding='utf-8') as src, \
     open('Test_Files/filtered_lines.txt', 'w', encoding='utf-8') as dst:
    for line in src:
        if keyword in line.lower():
            dst.write(line)

print('Created filtered_lines.txt')


# %%
'''
Homework 6 about reading/writing txt files:
Compute file statistics for "text_input.txt": number of lines, number of words, and number of characters
(excluding newline characters). Print the three numbers.
'''

lines = 0
words = 0
chars = 0
with open('Test_Files/text_input.txt', 'r', encoding='utf-8') as f:
    for line in f:
        lines += 1
        stripped = line.rstrip('\n')
        chars += len(stripped)
        words += len(stripped.split())

print('Lines:', lines)
print('Words:', words)
print('Chars (no \\n):', chars)


# %%
'''
Homework 7 about reading/writing txt files:
Merge two text files line-by-line into "merged_alternating.txt": write line 1 from file A, then line 1
from file B, then line 2 from file A, etc. If one file is longer, append its remaining lines at the end.
'''

from itertools import zip_longest

with open('Test_Files/file_a.txt', 'r', encoding='utf-8') as fa, \
     open('Test_Files/file_b.txt', 'r', encoding='utf-8') as fb, \
     open('Test_Files/merged_alternating.txt', 'w', encoding='utf-8') as out:
    for la, lb in zip_longest(fa, fb, fillvalue=''):
        if la:
            out.write(la)
        if lb:
            out.write(lb)

print('Created merged_alternating.txt')


# %%
'''
Homework 8 about reading/writing txt files:
Find-and-replace in a file without modifying the original: read "text_input.txt", replace all occurrences
of a target string with a replacement string (case-sensitive), and write to "replaced.txt".
'''

target = input('Target string to replace: ')
replacement = input('Replacement string: ')

with open('Test_File/text_input.txt', 'r', encoding='utf-8') as src:
    content = src.read()

content = content.replace(target, replacement)

with open('Test_File/replaced.txt', 'w', encoding='utf-8') as dst:
    dst.write(content)

print('Created replaced.txt')


# %%
'''
Homework 9 about reading/writing txt files:
Remove duplicate lines from "text_input.txt" while preserving the first occurrence order.
Write the result to "deduped.txt".
'''

seen = set()
with open('Test_Files/text_input.txt', 'r', encoding='utf-8') as src, \
     open('Test_Files/deduped.txt', 'w', encoding='utf-8') as dst:
    for line in src:
        if line not in seen:
            seen.add(line)
            dst.write(line)

print('Created deduped.txt')


# %%
'''
Homework 10 about reading/writing txt files:
Split a large file "big.txt" into multiple files with exactly N lines per chunk (last chunk may be shorter).
Ask the user for N and write output files as "big_part_1.txt", "big_part_2.txt", ...
'''

chunk_size = int(input('Enter number of lines per chunk: '))
part = 1
buffer = []

with open('Test_Files/big.txt', 'r', encoding='utf-8') as src:
    for line in src:
        buffer.append(line)
        if len(buffer) == chunk_size:
            with open(f'Test_Files/big_part_{part}.txt', 'w', encoding='utf-8') as dst:
                dst.writelines(buffer)
            buffer.clear()
            part += 1

if buffer:
    with open(f'Test_Files/big_part_{part}.txt', 'w', encoding='utf-8') as dst:
        dst.writelines(buffer)

print(f'Created {part} part file(s).')

# %%
'''
Delete only the output files created by the Reading/Writing TXT file homeworks.
Keeps the base input files: file.txt, file_a.txt, file_b.txt, text_input.txt, big.txt.
Also cleans up any big_part_x.txt files inside the Test_Files folder.
'''

import os

def cleanup_outputs():
    files_to_delete = [
        "Test_Files/new_file.txt",
        "Test_Files/word_freq.txt",
        "Test_Files/numbered_lines.txt",
        "Test_Files/filtered_lines.txt",
        "Test_Files/replaced.txt",
        "Test_Files/deduped.txt",
        "Test_Files/merged_alternating.txt"
    ]

    # Delete outputs in the current folder
    for file in files_to_delete:
        try:
            os.remove(file)
            print(f"Deleted {file}")
        except FileNotFoundError:
            pass

    # Check and clean Test_Files folder for big_part_x.txt
    folder = "Test_Files"
    if os.path.isdir(folder):
        for f in os.listdir(folder):
            if f.startswith("big_part_") and f.endswith(".txt"):
                try:
                    os.remove(os.path.join(folder, f))
                    print(f"Deleted {folder}/{f}")
                except FileNotFoundError:
                    pass

    print("Cleanup complete. Base input files kept.")

cleanup_outputs()

# %%
