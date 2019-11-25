def searchBinaryTree(arr, start, end, k):
    mid = int(start + (end-start)/2)
    if arr[mid] == k:
        return arr[mid]

    if k < arr[mid]:
        end = mid - 1
        return searchBinaryTree(arr, start, end, k)
    else:
        start = mid + 1
        return searchBinaryTree(arr, start, end, k)


arr = [-11, 2, 3, 14, 25]

start = 0
end = len(arr) - 1

print(searchBinaryTree(arr, start, end, 14))
