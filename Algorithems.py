# testing.py
from sorting import *
from searching import *

def test_sorting_algorithms():
    # Test case for bubble sort
    arr = [3, 2, 1, 5, 4]
    assert bubble_sort(arr) == [1, 2, 3, 4, 5], "Bubble Sort test case failed"
    
    # Test case for selection sort
    arr = [3, 2, 1, 5, 4]
    assert selection_sort(arr) == [1, 2, 3, 4, 5], "Selection Sort test case failed"
    
    # Test case for merge sort
    arr = [3, 2, 1, 5, 4]
    assert merge_sort(arr) == [1, 2, 3, 4, 5], "Merge Sort test case failed"
    
    # Test case for quick sort
    arr = [3, 2, 1, 5, 4]
    assert quick_sort(arr) == [1, 2, 3, 4, 5], "Quick Sort test case failed"

def test_searching_algorithms():
    # Test case for linear search
    arr = [3, 2, 1, 5, 4]
    assert linear_search(arr, 5) == 3, "Linear Search test case failed"
    
    # Test case for binary search
    sorted_arr = [1, 2, 3, 4, 5]
    assert binary_search(sorted_arr, 3) == 2, "Binary Search test case failed"
    
    # Test case for interpolation search
    sorted_arr = [1, 2, 3, 4, 5]
    assert interpolation_search(sorted_arr, 3) == 2, "Interpolation Search test case failed"
    
    # Test case for exponential search
    sorted_arr = [1, 2, 3, 4, 5]
    assert exponential_search(sorted_arr, 3) == 2, "Exponential Search test case failed"
    
    # Test case for jump search
    sorted_arr = [1, 2, 3, 4, 5]
    assert jump_search(sorted_arr, 3) == 2, "Jump Search test case failed"

if __name__ == "__main__":
    test_sorting_algorithms()
    test_searching_algorithms()
    print("All tests passed!")