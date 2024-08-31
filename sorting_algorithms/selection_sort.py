'''
Selection sort is a simple comparison sort that has
an average and worst-case time complexity of
O(n^2). It is inefficient on large lists, and 
generally worse than the insertion sort.
'''

def selection_sort(arr):
    # traverse through all array elements
    for i in range(len(arr)):
        # Find the minimum element in remaining unsorted array
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j

        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


arr = [64, 25, 12, 22, 11]
selection_sort(arr)
print("Sorted array is: ", arr)
