# %%
'''
Homework 1 about Try/Except:
Write a program that asks the user to enter an integer. Use try/except to catch ValueError
if the input is not an integer, and print "Invalid input".
'''

try:
    num = int(input("Enter an integer: "))
    print("You entered:", num)
except ValueError:
    print("Invalid input")


# %%
'''
Homework 2 about Try/Except:
Write a function divide(a, b) that returns a/b. Handle ZeroDivisionError by returning
"Cannot divide by zero".
'''

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"

print(divide(10, 2))
print(divide(5, 0))


# %%
'''
Homework 3 about Try/Except:
Write a program that opens a file "sample.txt" and prints its contents.
If the file does not exist, catch FileNotFoundError and print "File not found".
'''

try:
    with open("sample.txt", "r", encoding="utf-8") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found")


# %%
'''
Homework 4 about Try/Except:
Write a program that tries to convert a list of strings ["1", "2", "three", "4"] into integers.
Use try/except to skip items that cannot be converted. Print the list of valid integers.
'''

strings = ["1", "2", "three", "4"]
valid_ints = []

for s in strings:
    try:
        valid_ints.append(int(s))
    except ValueError:
        pass

print(valid_ints)


# %%
'''
Homework 5 about Try/Except:
Write a program that repeatedly asks the user for a number until they enter a valid integer.
Use try/except to handle invalid inputs.
'''

while True:
    try:
        num = int(input("Enter a valid integer: "))
        print("Thank you! You entered:", num)
        break
    except ValueError:
        print("Invalid input. Please try again.")


# %%
'''
Homework 6 about Try/Except:
Write a function safe_dict_access(d, key) that returns d[key].
If the key does not exist, catch the KeyError and return "Key not found".
'''

def safe_dict_access(d, key):
    try:
        return d[key]
    except KeyError:
        return "Key not found"

print(safe_dict_access({"a": 1, "b": 2}, "a"))
print(safe_dict_access({"a": 1, "b": 2}, "z"))


# %%
'''
Homework 7 about Try/Except:
Write a program that converts a string input into a float.
Handle both ValueError (invalid float) and TypeError (wrong type).
'''

def to_float(val):
    try:
        return float(val)
    except ValueError:
        return "ValueError: cannot convert to float"
    except TypeError:
        return "TypeError: invalid type"

print(to_float("3.14"))
print(to_float("abc"))
print(to_float(None))


# %%
'''
Homework 8 about Try/Except:
Write a program that divides two numbers entered by the user.
Handle both ValueError (non-numeric input) and ZeroDivisionError.
'''

try:
    a = float(input("Enter numerator: "))
    b = float(input("Enter denominator: "))
    print("Result:", a / b)
except ValueError:
    print("Error: Please enter numeric values.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")


# %%
'''
Homework 9 about Try/Except:
Write a program that tries to open "data.txt" for reading.
If the file doesn’t exist, create the file and write "New file created".
'''

try:
    with open("data.txt", "r", encoding="utf-8") as f:
        print(f.read())
except FileNotFoundError:
    with open("data.txt", "w", encoding="utf-8") as f:
        f.write("New file created")
    print("File not found. Created data.txt.")


# %%
'''
Homework 10 about Try/Except:
Write a function list_average(lst) that returns the average of numbers in lst.
If lst is empty, handle ZeroDivisionError and return "List is empty".
If lst contains non-numeric values, handle TypeError or ValueError.
'''

def list_average(lst):
    try:
        return sum(lst) / len(lst)
    except ZeroDivisionError:
        return "List is empty"
    except (TypeError, ValueError):
        return "List contains non-numeric values"

print(list_average([1, 2, 3, 4]))
print(list_average([]))
print(list_average([1, "a", 3]))
# %%
