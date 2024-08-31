'''
Bubble Sort - Revision and improving my capability

Errors: swap function requires an array to be parsed to be able to
modify its elements inside the bubble sort function

the firs loop determines the range for the search
the second loop do the actual search within the range
'''

def swap(arr, x, y):
    arr[x], arr[y] = arr[y], arr[x]

def opt_bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        #print('this is i: ',i)
        for j in range(0, n-i-1):
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
