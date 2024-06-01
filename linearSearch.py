
def linear_search(arr, target):
    """
    Perform a linear search for the target value in the array.
    :param arr: List of elements to search
    :param target: The target value to search for
    :return: The index of the target value if found, otherwise -1
    """
    for index in range(len(arr)):
        if arr[index] == target:
            return index
    return -1

# array 
arr = [10,23,45,70,11,15]
target = 70
result = linear_search(arr, target)

if result != -1:
    print(f'Element found at index {result}')
else:
    print(f'Element not found in the array')
