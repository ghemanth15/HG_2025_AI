# %%
'''
JUST FOR MAKING THE DATA EASY!!!
________________________________
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



# %%
'''
Homework 2 about reading/writing txt files:
Make a txt file and write 10 lines of text in it (anything). Read the file in Python and write a new
txt file that includes every other line from the first file: lines 1, 3, 5, 7, and 9.
'''



# %%
'''
Homework 3 about reading/writing txt files:
Read a text file and produce a new file "word_freq.txt" that lists each distinct word (case-insensitive)
and its count, sorted by descending count then ascending word. Ignore punctuation next to words.
'''



# %%
'''
Homework 4 about reading/writing txt files:
Read a text file and write a new file where each line is prefixed with its 1-based line number
(e.g., "1: <line>"). Save as "numbered_lines.txt".
'''



# %%
'''
Homework 5 about reading/writing txt files:
Ask the user for a keyword, then read "text_input.txt" and write all lines containing that keyword
(case-insensitive) to "filtered_lines.txt".
'''



# %%
'''
Homework 6 about reading/writing txt files:
Compute file statistics for "text_input.txt": number of lines, number of words, and number of characters
(excluding newline characters). Print the three numbers.
'''



# %%
'''
Homework 7 about reading/writing txt files:
Merge two text files line-by-line into "merged_alternating.txt": write line 1 from file A, then line 1
from file B, then line 2 from file A, etc. If one file is longer, append its remaining lines at the end.
'''



# %%
'''
Homework 8 about reading/writing txt files:
Find-and-replace in a file without modifying the original: read "text_input.txt", replace all occurrences
of a target string with a replacement string (case-sensitive), and write to "replaced.txt".
'''



# %%
'''
Homework 9 about reading/writing txt files:
Remove duplicate lines from "text_input.txt" while preserving the first occurrence order.
Write the result to "deduped.txt".
'''




# %%
'''
Homework 10 about reading/writing txt files:
Split a large file "big.txt" into multiple files with exactly N lines per chunk (last chunk may be shorter).
Ask the user for N and write output files as "big_part_1.txt", "big_part_2.txt", ...
'''

