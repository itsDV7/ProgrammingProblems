def partition(arr, left, right):
    mid = left
    pivot = arr[right]
    
    while mid <= right:
        if arr[mid] < pivot:
            arr[left], arr[mid] = arr[mid], arr[left]
            left += 1
            mid += 1
        elif arr[mid] > pivot:
            arr[mid], arr[right] = arr[right], arr[mid]
            right -= 1
        else:
            mid += 1
    return left - 1, mid

def quick_sort(arr, left, right):
    if left < right:
        i, j = partition(arr, left, right)
        quick_sort(arr, left, i)
        quick_sort(arr, j, right)
        
if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    quick_sort(arr, 0, len(arr)-1)
    print(*arr)
