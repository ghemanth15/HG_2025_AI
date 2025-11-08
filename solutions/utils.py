def power(base, exp):
    return base ** exp

def hello(name):
    print(f"Hello, {name}!")

def area_rectangle(l, w):
    return l * w

def perimeter_rectangle(l, w):
    return 2 * (l + w)

def word_count(s):
    return len(s.split())

def median(lst):
    lst_sorted = sorted(lst)
    n = len(lst_sorted)
    mid = n // 2
    if n % 2 == 0:
        return (lst_sorted[mid - 1] + lst_sorted[mid]) / 2
    else:
        return lst_sorted[mid]
