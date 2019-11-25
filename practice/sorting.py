"""
All sorting algorithms
"""


def bubblesort(arr):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True
    return arr


def insertionsort(arr):
    for i in range(len(arr)):
        temp = arr[i]
        j = i-1
        while j >= 0 and arr[j] > temp:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = temp
    return arr


def quicksort(arr):
    less = []
    equal = []
    greater = []

    if len(arr) > 1:
        pivot = arr[0]
        for element in arr:
            if element < pivot:
                less.append(element)
            if element > pivot:
                greater.append(element)
            if element == pivot:
                equal.append(element)
        return quicksort(less) + equal + quicksort(greater)
    else:
        return arr


def selectionsort(arr):
    for i in range(len(arr)):
        lowest = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[lowest]:
                lowest = j

        arr[i], arr[lowest] = arr[lowest], arr[i]
    return arr


input = [5, 4, 3, 2, 1]
print("Input List:\t\t\t{}".format(input))
print("Bubble Sort:\t\t{}".format(bubblesort(input)))
print("Insertion Sort:\t\t{}".format(insertionsort(input)))
print("Quick Sort:\t\t\t{}".format(quicksort(input)))
print("Selection Sort:\t\t{}".format(selectionsort(input)))
