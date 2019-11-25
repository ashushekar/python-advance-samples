"""
Find four elements a, b, c and d in an array such that a+b = c+d.
Given an array of distinct integers, find if there are two pairs
(a, b) and (c, d) such that a+b = c+d, and a, b, c and d are distinct
elements. If there are multiple answers, then print any of them.

Expected Time Complexity: O(n2)

Input:   {3, 4, 7, 1, 2, 9, 8}
Output:  (3, 8) and (4, 7)
Explanation: 3+8 = 4+7

Input:  {65, 30, 7, 90, 1, 9, 8};
Output:  No pairs found

Solution: An Efficient Solution can solve this problem in O(n2) time. The idea is
to use hashing. We use sum as key and pair as value in hash table.
"""


def sumpairs(arr):
    Hash = {}
    n = len(arr)

    for i in range(n-1):
        for j in range(i+1, n):
            sum = arr[i] + arr[j]
            if sum in Hash.keys():
                prev = Hash.get(sum)
                print("{0} and ({1}, {2})".format(prev, arr[i], arr[j]))
                return True
            else:
                Hash[sum] = (arr[i], arr[j])
    print("No pairs found")
    return False


arr1 = [3, 4, 7, 1, 2, 9, 8]
sumpairs(arr1)

arr2 = [65, 30, 7, 90, 1, 9, 8]
sumpairs(arr2)