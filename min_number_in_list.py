import time
from random import randrange


def find_min1(alist):  # sourcery skip: invert-any-all, use-any
    """
    Quadratic time complexity i.e O(n^2).
    """
    min_value = alist[0]
    for i in alist:
        is_min_value = True

        for j in alist:
            if i > j:
                is_min_value = False
        if is_min_value:
            min_value = i
    return min_value


def find_min2(alist): # better than above function
    """
    Linear time complexity i.e O(n).
    """
    min_value = alist[0]
    for i in alist:
        if i < min_value:
            min_value = i
    return min_value


# print(find_min([6, 1, 5, 3, 0]))
# print(find_min([0, 1, 5, 3, 6]))
# print(find_min([8, 1, 5, 3, 6]))

for list_size in range(1000, 10001, 1000):
    alist = [randrange(100000) for _ in range(list_size)]
    print("===========================================================")
    start = time.time()
    print(find_min1(alist))
    end = time.time()
    print()
    print(f"find_min1: size: {list_size} time: {end - start} seconds")

    print()
    start = time.time()
    print(find_min2(alist))
    end = time.time()
    print()
    print(f"find_min2: size: {list_size} time: {end - start} seconds")



