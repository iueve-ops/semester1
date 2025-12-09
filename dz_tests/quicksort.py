def quicksort(arr):
    if not isinstance(arr, list):
        raise TypeError("введи набор чисел list")
    for x in arr:
        if not isinstance(x, (int, float)):
            raise TypeError("элементы введены непраильно")

    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]

    left = []
    mid = []
    right = []

    for x in arr:
        if x < pivot:
            left.append(x)
        elif x == pivot:
            mid.append(x)
        else:
            right.append(x)

    return quicksort(left) + mid + quicksort(right)
