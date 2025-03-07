def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def order_statistic(arr, low, high, i):
    if low <= high:
        pi = partition(arr, low, high)
        if pi == i:
            return arr[pi]
        elif pi > i:
            return order_statistic(arr, low, pi - 1, i)
        else:
            return order_statistic(arr, pi + 1, high, i)
    return None

# Example usage
arr = [7, 10, 4, 7, 20, 15]
i = 3  # We want the 3rd smallest element (index 2)
result = order_statistic(arr, 0, len(arr) - 1, i - 1)  # i-1 for 0-based index
print(f"The {i}th smallest element is: {result}")
