"""
This simple sorting algorithm iterates over a list, comparing elements in pairs and swapping
them until the larger elements "bubble up" to the end of the list, and the smaller elements
stay at the "bottom".

Time Complexity
In the worst case scenario (when the list is in reverse order), this algorithm would have to
swap every single item of the array. Our swapped flag would be set to True on every iteration.
Therefore, if we have n elements in our list, we would have n iterations per item - thus Bubble
Sort's time complexity is O(n^2).
"""


def bubblesort(arr):

    swapped = True
    while swapped:
        swapped = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i + 1] = arr[i+1], arr[i]
                swapped = True
    return arr


input = [5, 4, 3, 2, 1]
print(bubblesort(input))
