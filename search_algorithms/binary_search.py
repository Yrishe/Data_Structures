

def binarySearch(arr,target):
    n = len(arr)
    L = 0
    R = n-1
    while(R >= L):
        mid = (L+R)//2
        if(arr[mid] == target):
            return mid
        elif(arr[mid] > target):
            R = mid-1
        else:
            L = mid+1
    return False

ls = [5,1,7,23,9,3,1,0,6]

'''It is not ideal to run binary search on list that isn't sorted 
Therefore, we have to sort it before begining any search. But we need 
to consider one thing first. The time complexity. We could sort it 
with any sorting algorithm and done. But if we don't pick the quickest
strategy, it won't achieve the best efficiency.

For this reason, let's use merge sort because differently from bubblesort,
and insertion sort, it worst-case time complexity is O(nlogn).
''' 

def Merge(w,v):
    m = len(w)
    n = len(v)
    s = []
    i, j, k = 0,0,0
    while((i < m) and (j < n)):
        if(w[i] < v[j]):
            s.append(w[i])
            i += 1
        else:
            s.append(v[j])
            j += 1
        k += 1
    while(i < m):
        s.append(w[i])
        i += 1 
        k += 1
    while(j < n):
        s.append(v[j])
        j += 1
        k += 1
    return s

def MergeSort(vector):
    n = len(vector)
    if(n == 1):
        return vector
    m = (n+1)//2
    L = vector[:m]
    R = vector[m:]
    return Merge(MergeSort(L), MergeSort(R))

print(ls)
# return [5,1,7,23,9,3,1,0,6]
print(f'Sorting list: {MergeSort(ls)}')
# return [0,1,1,3,5,6,7,9,23]
print(f'Searching for number 60: {binarySearch(ls, 60)}')
# return False
