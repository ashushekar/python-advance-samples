"""
Convert an array to reduced form | Set 1 (Simple and Hashing)
Given an array with n distinct elements, convert the given array to a form
where all elements are in range from 0 to n-1. The order of elements is same,
i.e., 0 is placed in place of smallest element, 1 is placed for second smallest
element, … n-1 is placed for largest element.

Input:  arr[] = {10, 40, 20}
Output: arr[] = {0, 2, 1}

Input:  arr[] = {5, 10, 40, 30, 20}
Output: arr[] = {0, 1, 4, 3, 2}
"""


def reducedform(arr):
    temp = [arr[i] for i in range(len(arr))]
    temp.sort()
    umap = {}

    val = 0
    for i in range(len(arr)):
        umap[temp[i]] = val
        val += 1

    for i in range(len(arr)):
        arr[i] = umap[arr[i]]
    print(arr)


arr = [24, 32, 12, 10, 2, 56]

reducedform(arr)
