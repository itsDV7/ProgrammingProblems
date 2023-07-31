array = [5,7,9,2,4,6,1,3,10,8]

# Selection Sort - Select Min, Swap to place
def selection_sort(arr):
    left = 0
    right = 0
    while left < len(arr):
        min_index = right
        while right < len(arr):
            if arr[right] < arr[min_index]:
                min_index = right
            right += 1
        arr[left], arr[min_index] = arr[min_index], arr[left]
        left += 1
        right = left
    print("Selection Sort -", arr)
selection_sort([a for a in array])

# Bubble Sort - Swap with next if prev is larger
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    print("Bubble Sort -", arr)
bubble_sort([a for a in array])

# Insertion Sort - Insert to place in traversed array
def insertion_sort(arr):
    for i in range(len(arr) - 1):
        while i >= 0 and arr[i+1] < arr[i]:
            arr[i+1], arr[i] = arr[i], arr[i+1]
            i -= 1
    print("Insertion Sort -", arr)
insertion_sort([a for a in array])

# Merge Sort - Divide and Sort - Inversion Count Problem
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        
        merge_sort(left)
        merge_sort(right)
        
        i = j = k = 0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

merge_sort_arr = [a for a in array]
merge_sort(merge_sort_arr)
print("Merge Sort -", merge_sort_arr)

# Quick Sort - Select Pivot, Divide, and Sort
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1

def quick_sort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        quick_sort(arr, low, p-1)
        quick_sort(arr, p+1, high)
        
quick_sort_arr = [a for a in array]
quick_sort(quick_sort_arr, 0, len(quick_sort_arr)-1)
print("Quick Sort -", quick_sort_arr)


print("Original Arr -", array)

