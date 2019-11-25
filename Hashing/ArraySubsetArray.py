"""
Find whether an array is subset of another array
Given two arrays: arr1[0..m-1] and arr2[0..n-1]. Find whether arr2[] is a subset of arr1[]
or not. Both the arrays are not in sorted order. It may be assumed that elements in both
array are distinct.

Input: arr1[] = {1, 2, 3, 4, 5, 6}, arr2[] = {1, 2, 4}
Output: arr2[] is a subset of arr1[]

Input: arr1[] = {10, 5, 2, 23, 19}, arr2[] = {19, 5, 3}
Output: arr2[] is not a subset of arr1[]
"""


def checksubset(arr1, arr2):
    m = len(arr1)
    n = len(arr2)
    j = 0
    for i in range(n):
        for j in range(m):
            if arr2[i] == arr1[j]:
                break

        if j == m:
            return 0
    return 1


arr1 = [1, 2, 3, 4, 5, 6]
arr2 = [1, 7, 4]

if checksubset(arr1, arr2):
    print("arr2[] is subset of arr1[] ")
else:
    print("arr2[] is not a subset of arr1[]")
