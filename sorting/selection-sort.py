"""
What we do is treat the leftmost part of the list as the sorted segment. We then search the entire
list for the smallest element, and swap it with the first element.

Now we know that the first element of the list is sorted, we get the smallest element of the remaining
items and swap it with the second element. This iterates until the last item of the list is remaining
element to be examined.

Time Complexity
We can easily get the time complexity by examining the for loops in the Selection Sort algorithm. For
a list with n elements, the outer loop iterates n times. The inner loop iterate n-1 when i is equal to
1, and then n-2 as i is equal to 2 and so forth.

The amount of comparisons are (n - 1) + (n - 2) + ... + 1, which gives the Selection Sort a time
complexity of O(n^2).
"""


def selectionsort(arr):
    for i in range(len(arr)):
        lowest_value_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[lowest_value_index]:
                lowest_value_index = j

        arr[i], arr[lowest_value_index] = arr[lowest_value_index], arr[i]
    return arr


input = [56, 4, 3, 2, 1]
print(selectionsort(input))
