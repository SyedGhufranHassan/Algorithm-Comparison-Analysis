# searching.py
def linear_search(arr, target):
    """
    Searches for the target element in the input array using Linear Search algorithm.
    
    Parameters:
    arr (list): The input list to be searched.
    target: The element to search for in the array.
    
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
        # Returns:  int: The index of the target element if found, else -1.
    return -1

def binary_search(arr, target):
    """
    Searches for the target element in the input array using Binary Search algorithm.
    
    Parameters:
    arr (list): The input list to be searched (must be sorted).
    target: The element to search for in the array.
    
    """
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
            
        # Returns: int: The index of the target element if found, else -1.    
    return -1

def interpolation_search(arr, target):
    """
    Searches for the target element in the input array using Interpolation Search algorithm.
    
    Parameters:
    arr (list): The input list to be searched (must be sorted).
    target: The element to search for in the array.
    
    """
    low = 0
    high = len(arr) - 1
    while low <= high and target >= arr[low] and target <= arr[high]:
        pos = low + ((high - low) // (arr[high] - arr[low])) * (target - arr[low])
        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1
        # Returns: int: The index of the target element if found, else -1.
    return -1

def exponential_search(arr, target):
    """
    Searches for the target element in the input array using Exponential Search algorithm.
    
    Parameters:
    arr (list): The input list to be searched (must be sorted).
    target: The element to search for in the array.
    
    """
    if arr[0] == target:
        return 0
    n = len(arr)
    i = 1
    while i < n and arr[i] <= target:
        i *= 2
        
    # Returns: int: The index of the target element if found, else -1.    
    return binary_search(arr, target)

def jump_search(arr, target):
    """
    Searches for the target element in the input array using Jump Search algorithm.
    
    Parameters:
    arr (list): The input list to be searched (must be sorted).
    target: The element to search for in the array.
    
    """
    n = len(arr)
    step = int(n ** 0.5)
    prev = 0
    while arr[min(step, n) - 1] < target:
        prev = step
        step += int(n ** 0.5)
        if prev >= n:
            return -1
    while arr[prev] < target:
        prev += 1
        if prev == min(step, n):
            return -1
    if arr[prev] == target:
        return prev
    # Returns: int: The index of the target element if found, else -1.
    return -1