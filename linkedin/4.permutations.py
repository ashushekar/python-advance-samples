def permutation(arr):

    if len(arr) == 0:
        return []

    if len(arr) == 1:
        return [arr]

    l = []
    for i in range(len(arr)):
        m = arr[i]

        lst = arr[:i] + arr[i+1:]

        for p in permutation(lst):
            l.append([m] + p)

    return l


print(permutation([2,4,5,10]))