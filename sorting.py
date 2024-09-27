#Sorting
def bubble_sort(arr):
    """
    Sorts the input array using Bubble Sort.
    
    Parameters:
    arr (list): The input list to be sorted.
    
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    #Returns:The sorted list.
    return arr

def selection_sort(arr):
    """
    Sorts the input array using Selection Sort algorithm.
    
    Parameters:
    arr (list): The input list to be sorted.
    
    """
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    # Returns: The sorted list.
    return arr

def insertion_sort(arr):
    """
    Sorts the input array using Insertion Sort algorithm.
    
    Parameters:
    arr (list): The input list to be sorted.
    
    """
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    # Returns: The sorted list.
    return arr

def merge_sort(arr):
    """
    Sorts the input array using Merge Sort algorithm.
    
    Parameters:
    arr (list): The input list to be sorted.
    
    """
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
            
    # Returns: The sorted list.
    return arr


def quick_sort(arr):
    """
    Sorts the input array using Quick Sort algorithm.
    
    Parameters:
    arr (list): The input list to be sorted.

    """
    # Implementation of Quick Sort
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    # Returns: The sorted list.
    return quick_sort(left) + middle + quick_sort(right)

