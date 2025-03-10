from asyncio import base_tasks
import math
import time
import random

"""
See below for mergeSort and countSort functions, and for a useful helper function.
In order to run your experiments, you may find the functions random.randint() and time.time() useful.

In general, for each value of n and each universe size 'U' you will want to
    1. Generate a random array of length n whose keys are in 0, ..., U - 1
    2. Run count sort, merge sort, and radix sort ~10 times each,
       averaging the runtimes of each function. 
       (If you are finding that your code is taking too long to run with 10 repitions, you should feel free to decrease that number)

To graph, you can use a library like matplotlib or simply put your data in a Google/Excel sheet.
A great resource for all your (current and future) graphing needs is the Python Graph Gallery 
"""


def merge(arr1, arr2):
    sortedArr = []

    i = 0
    j = 0
    while i < len(arr1) or j < len(arr2):
        if i >= len(arr1):
            sortedArr.append(arr2[j])
            j += 1
        elif j >= len(arr2):
            sortedArr.append(arr1[i])
            i += 1
        elif arr1[i][0] <= arr2[j][0]:
            sortedArr.append(arr1[i])
            i += 1
        else:
            sortedArr.append(arr2[j])
            j += 1

    return sortedArr


def mergeSort(arr):
    if len(arr) < 2:
        return arr

    midpt = int(math.ceil(len(arr) / 2))

    half1 = mergeSort(arr[0:midpt])
    half2 = mergeSort(arr[midpt:])

    return merge(half1, half2)


def countSort(univsize, arr):
    universe = []
    for i in range(univsize):
        universe.append([])

    for elt in arr:
        universe[elt[0]].append(elt)

    sortedArr = []
    for lst in universe:
        for elt in lst:
            sortedArr.append(elt)

    return sortedArr


def BC(n, b, k):
    if b < 2:
        raise ValueError()
    digits = []
    for i in range(k):
        digits.append(n % b)
        n = n // b
    if n > 0:
        raise ValueError()
    return digits


def radixSort(univsize, base, arr):
    # Following pseudocode
    k = math.ceil(math.log(univsize, base))
    n = len(arr)
    values2 = [None] * n
    for i in range(n):
        values2[i] = BC(arr[i][0], base, k)

    toSort = [None] * n
    for i in range(n):
        toSort[i] = (arr[i][0], arr[i][1], values2[i])
    for j in range(k):
        keys2 = [0] * n
        for i in range(n):
            keys2[i] = values2[i][j]
            # Generate list with values2 (V') to call counting sort on
            toSort[i] = (keys2[i], arr[i][1], values2[i])
        toSort = countSort(base, toSort)

    ans = []
    for i in range(n):
        key = 0
        baseFactor = 1
        for j in range(k):
            key += toSort[i][2][j] * baseFactor
            baseFactor *= base
        ans.append((key, toSort[i][1]))

    return ans


# print(radixSort(100, 10, [(10, 1), (12, 1), (33, 1), (21, 1), (15, 1), (61, 1)]))
