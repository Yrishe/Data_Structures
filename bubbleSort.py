'''
Bubble Sort - Revision and improving my capability
'''

def swap(arr, x, y):
    arr[x], arr[y] = arr[y], arr[x]

def opt_bubble_sort(arr):
    n = len(arr)
    for i in range(n): # determines the range
        swapped = False
        #print('this is i: ',i)
        for j in range(0, n-i-1): # performs the search
           #print('this is j: ',j)
           if arr[j] > arr[j+1]: 
               swap(arr, j, j+1)
               swapped = True
        if not swapped:
            break

# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
opt_bubble_sort(arr)
print("Sorted array is:", arr)
