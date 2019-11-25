"""
We assume that the first element of the list is sorted. We then go to the next element,
let's call it x. If x is larger than the first element we leave as is. If x is smaller,
we copy the value of the first element to the second position and then set the first
element to x.

As we go to the other elements of the unsorted segment, we continuously move larger elements
in the sorted segment up the list until we encounter an element smaller than x or reach the
end of the sorted segment, and then place x in it's correct position.

Time Complexity
In the worst case scenario, an array would be sorted in reverse order. The outer for loop
in the Insertion Sort function always iterates n-1 times.

In the worst case scenario, the inner for loop would swap once, then swap two and so forth.
The amount of swaps would then be 1 + 2 + ... + (n - 3) + (n - 2) + (n - 1) which gives the
Insertion Sort a time complexity of O(n^2).
"""


def insertionsort(arr):
    for i in range(1, len(arr)):
        items_to_insert = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > items_to_insert:
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = items_to_insert
    return arr


input = [56, 4, 3, 2, 1]
print(insertionsort(input))
