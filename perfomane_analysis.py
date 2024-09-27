import time
import random
from sorting import *
from searching import *

# Generate arrays of varying sizes
sizes = [10, 100, 1000, 10000, 100000, 1000000, 5000000]

# Sorting algorithms performance analysis
for size in sizes:
    arr = [random.randint(0, 1000) for _ in range(size)]
    
    start_time = time.time()
    bubble_sort(arr.copy())
    end_time = time.time()
    bubble_time = end_time - start_time
    
    start_time = time.time()
    selection_sort(arr.copy())
    end_time = time.time()
    selection_time = end_time - start_time
    
    start_time = time.time()
    insertion_sort(arr.copy())
    end_time = time.time()
    insertion_time = end_time - start_time
    
    start_time = time.time()
    merge_sort(arr.copy())
    end_time = time.time()
    merge_time = end_time - start_time
    
    start_time = time.time()
    quick_sort(arr.copy())
    end_time = time.time()
    quick_time = end_time - start_time
    
    print(f"Array size: {size}")
    print(f"Bubble Sort time: {bubble_time} seconds")
    print(f"Selection Sort time: {selection_time} seconds")
    print(f"Insertion Sort time: {insertion_time} seconds")
    print(f"Merge Sort time: {merge_time} seconds")
    print(f"Quick Sort time: {quick_time} seconds")
    print()

# Searching algorithms performance analysis
for size in sizes:
    arr = sorted([random.randint(0, 1000) for _ in range(size)])
    target = random.randint(0, 1000)
    
    start_time = time.time()
    linear_search(arr, target)
    end_time = time.time()
    linear_time = end_time - start_time
    
    start_time = time.time()
    binary_search(arr, target)
    end_time = time.time()
    binary_time = end_time - start_time
    
    start_time = time.time()
    interpolation_search(arr, target)
    end_time = time.time()
    interpolation_time = end_time - start_time
    
    start_time = time.time()
    exponential_search(arr, target)
    end_time = time.time()
    exponential_time = end_time - start_time
    
    start_time = time.time()
    jump_search(arr, target)
    end_time = time.time()
    jump_time = end_time - start_time
    
    print(f"Array size: {size}")
    print(f"Linear Search time: {linear_time} seconds")
    print(f"Binary Search time: {binary_time} seconds")
    print(f"Interpolation Search time: {interpolation_time} seconds")
    print(f"Exponential Search time: {exponential_time} seconds")
    print(f"Jump Search time: {jump_time} seconds")
    print()