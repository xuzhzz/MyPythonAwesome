array = [7, 5, 6, 3, 8, 2, 1]


def quicksort(arr):
    if not arr:
        return []
    return quicksort([a1 for a1 in arr[1:] if a1 <= arr[0]]) + [arr[0]] + quicksort(
        [a1 for a1 in arr[1:] if a1 > arr[0]])


arr2 = quicksort(array)
print(arr2)
