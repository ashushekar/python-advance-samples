"""
Given an array of size n and an integer k, return the of count of distinct numbers in all windows of size k.
Example:

Input: arr[] = {1, 2, 1, 3, 4, 2, 3};
k = 4
Output:
3
4
4
3

Explanation:
First window is {1, 2, 1, 3}, count of distinct numbers is 3
Second window is {2, 1, 3, 4} count of distinct numbers is 4
Third window is {1, 3, 4, 2} count of distinct numbers is 4
Fourth window is {3, 4, 2, 3} count of distinct numbers is 3

Efficient solution is using mapping O(nk)
"""


def countWindowDistinct(win, k):
    dist_count = 0

    for i in range(k):
        j = 0
        while j < i:
            if win[i] == win[j]:
                break
            else:
                j += 1
        if j == i:
            dist_count += 1

    return dist_count


def countDistinct(arr, n, k):
    # Traverse through every window
    for i in range(n - k + 1):
        print(countWindowDistinct(arr[i:k + i], k))


arr1 = [1, 2, 1, 3, 4, 2, 3]
k = 4

countDistinct(arr1, len(arr1), k)
