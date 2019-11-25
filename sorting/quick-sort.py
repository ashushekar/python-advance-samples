"""
Like Merge Sort, QuickSort is a Divide and Conquer algorithm. It picks an element as
pivot and partitions the given array around the picked pivot. There are many different
versions of quickSort that pick pivot in different ways.

1. Always pick first element as pivot.
2. Always pick last element as pivot (implemented below)
3. Pick a random element as pivot.
4. Pick median as pivot.

The key process in quickSort is partition(). Target of partitions is, given an array
and an element x of array as pivot, put x at its correct position in sorted array and
put all smaller elements (smaller than x) before x, and put all greater elements
(greater than x) after x. All this should be done in linear time.
"""


def quicksort(arr):
    less = []
    equal = []
    greater = []

    if len(arr) > 1:
        pivot = arr[0]
        for e in arr:
            if e < pivot:
                less.append(e)
            if e == pivot:
                equal.append(e)
            if e > pivot:
                greater.append(e)
        return quicksort(less) + equal + quicksort(greater)
    else:
        return arr


array = [12, 4, 5, 6, 7, 3, 1, 15]
print(quicksort(array))
