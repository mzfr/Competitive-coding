def hoare_partition(arr: list, low: int, high: int):
    """This function takes first element as pivot, and places
    all the elements smaller than the pivot on the left side
    and all the elements greater than the pivot on
    the right side. It returns the index of the last element
    on the smaller side
    """
    pivot = arr[low]
    i = low - 1
    j = high + 1

    while True:
        i += 1
        while arr[i] < pivot:
            i += 1

        j -= 1
        while arr[j] > pivot:
            j -= 1

        if i >= j:
            return j

        arr[i], arr[j] = arr[j], arr[i]


def Lomuto_partition(arr: list, low: int, high: int):
    """This function takes last element as pivot, places
    the pivot element at its correct position in sorted
    array, and places all smaller (smaller than pivot)
    to left of pivot and all greater elements to right
    of pivot
    """
    i = low - 1
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quicksort(arr: list, low: int, high: int):
    if low < high:
        pivot = Lomuto_partition(arr, low, high)
        # pivot = hoare_partition(arr, low, high)
        quicksort(arr, low, pivot - 1)
        quicksort(arr, pivot + 1, high)


if __name__ == "__main__":
    arr = [18, 12, 2, 4, 32, 89, 92, 67, 87]
    quicksort(arr, 0, len(arr) - 1)
    print(arr)
