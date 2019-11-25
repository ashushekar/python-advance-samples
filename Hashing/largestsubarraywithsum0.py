"""
Find the length of largest subarray with 0 sum
Given an array of integers, find the length of the longest subarray with sum equals to 0.

Input: arr[] = {15, -2, 2, -8, 1, 7, 10, 23};
Output: 5
The largest subarray with 0 sum is -2, 2, -8, 1, 7

Time complexity of this method is O(n^2)
"""


def largestsubarray(arr):
    max_len = 0
    for i in range(len(arr)):
        sum = 0
        for j in range(i, len(arr)):
            sum += arr[j]

            if sum == 0:
                max_len = max(max_len, j-i+1)

    return max_len


arr1 = [15, -2, 2, -8, 1, 7, 10, 23]
print(largestsubarray(arr1))

