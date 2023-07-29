arr = [5,7,9,2,4,6,1,3,8,10]

# Selection Sort
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
    print("Selection Sort - ", arr)
selection_sort(arr)

