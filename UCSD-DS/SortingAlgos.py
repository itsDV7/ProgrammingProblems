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
print("Quick Sort Last Pivot -", quick_sort_arr)

def partition(arr, low, high):
    pivot = arr[low]
    i = low
    for j in range(low + 1, high + 1):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i], arr[low] = arr[low], arr[i]
    
    return i

def quick_sort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        quick_sort(arr, low, p-1)
        quick_sort(arr, p+1, high)

quick_sort_arr = [a for a in array]
quick_sort(quick_sort_arr, 0, len(quick_sort_arr)-1)
print("Quick Sort First Pivot -", quick_sort_arr)

from random import randint
def partition(arr, low, high):
    rand = randint(low, high)
    arr[high], arr[rand] = arr[rand], arr[high]
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        quick_sort(arr, low, p - 1)
        quick_sort(arr, p + 1, high)

quick_sort_arr = [a for a in array]
quick_sort(quick_sort_arr, 0, len(quick_sort_arr)-1)
print("Quick Sort Random Pivot -", quick_sort_arr)

# Heap Sort - Make tree and swap
def heapify(arr, index):
    swap_index = index
    left = 2 * index + 1
    right = 2 * index + 2
    if left < len(arr) and arr[left] < arr[swap_index]:
        swap_index = left
    if right < len(arr) and arr[right] < arr[swap_index]:
        swap_index = right
    if index != swap_index:
        arr[index], arr[swap_index] = arr[swap_index], arr[index]
        heapify(arr, swap_index)

def heap_sort(arr):
    for i in range(len(arr)//2-1, -1, -1):
        heapify(arr, i)
    sorted_arr = []
    for i in range(len(arr)-1):
        arr[0], arr[-1] = arr[-1], arr[0]
        sorted_arr.append(arr.pop())
        heapify(arr, 0)
    sorted_arr.append(arr.pop())
    print("Heap Sort Heapify -", sorted_arr)

heap_sort([a for a in array])

# Counting Sort - Assuming range 1 till 10
def counting_sort(arr):
    freq = [0]*(max(arr)+1)
    for a in arr:
        freq[a] += 1
    freq_ans = list()
    for i,f in enumerate(freq):
        if f:
            freq_ans.extend([i]*f)
    print("Counting Sort Freq -", freq_ans)
    for i in range(len(freq)-1):
        freq[i+1] += freq[i]
    sum_ans = [0]*len(arr)
    for a in arr:
        sum_ans[freq[a]-1] = a
        freq[a] -= 1
    print("Counting Sort CumSum -", sum_ans)

counting_sort([a for a in array])

# Radix Sort - Stable sort to 
print("Radix Array -", [170, 45, 75, 90, 802, 24, 2, 66])

def counting_sort_digit(arr, place):
    temp = [a for a in arr]
    for _ in range(place):
        temp = [t//10 for t in temp]
    temp = [t%10 for t in temp]
    freq = [0]*(max(temp)+1)
    for t in temp:
        freq[t] += 1
    for i in range(len(freq)-1):
        freq[i+1] += freq[i]
    sort = [0]*len(temp)
    for i, t in enumerate(temp[::-1]):
        sort[freq[t]-1] = arr[len(temp)-1-i]
        freq[t]-=1
    return sort

def radix_sort(arr):
    largest_num = max(arr)
    num_digits = 0
    while largest_num:
        num_digits += 1
        largest_num //= 10
    for i in range(num_digits):
        arr = counting_sort_digit(arr, i)
    print("Radix Sort -", arr)

radix_sort([170, 45, 75, 90, 802, 24, 2, 66])
