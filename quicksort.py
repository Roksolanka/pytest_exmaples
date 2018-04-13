import datetime
import sys
sys.setrecursionlimit(1500)

arr = [9, 8, 7, 6, 5, 0, 4, 3, 2, 1]


def sort(array=[9, 8, 7, 2, 4, 11]):
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)
        # Don't forget to return something!
        return sort(less) + equal + sort(greater)
    # Note that you want equal ^^^^^ not pivot
    else:
        return array


before_sort = datetime.datetime.now()
sort(arr)
print datetime.datetime.now() - before_sort


def qsort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
        lesser = qsort([x for x in array[1:] if x < pivot])
        greater = qsort([x for x in array[1:] if x >= pivot])
        return lesser + [pivot] + greater


before_qsort = datetime.datetime.now()
qsort(arr)
print datetime.datetime.now() - before_qsort

before_sorted = datetime.datetime.now()
print arr.sort()
print datetime.datetime.now() - before_sorted
