"""
Given an array A[] and a number x, check for pair in A[] with sum as x.
Write a program that, given an array A[] of n numbers and another number x,
determines whether or not there exist two elements in S whose sum is exactly x.
"""


def sumpair(arr, n):
    output = []
    temp = arr
    temp.sort()
    while True:
        left = 0
        right = len(arr) - 1
        while True:
            result = temp[left] + temp[right]
            if result > n:
                right -= 1
            elif result < n:
                left += 1
            else:
                output.append([temp[left], temp[right]])
                temp.remove(temp[left])
                temp.remove(temp[right])
            if left == right:
                return output


arr = [1, 4, 45, 6, 10, -8, 12, 11, 5, 3]
n = 56

pairs = sumpair(arr, n)
print(pairs)
