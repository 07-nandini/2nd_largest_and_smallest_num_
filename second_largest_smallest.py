def second_smallest_and_largest(arr):
    arr = sorted(set(arr))
    if len(arr) < 2:
        return -1, -1
    second_smallest = arr[1]
    second_largest = arr[-2]
    
    return second_smallest, second_largest


arr1 = [1, 2, 4, 7, 7, 5]
arr2 = [1]
print("Second Smallest and largest for arr1:", second_smallest_and_largest(arr1))
print("Second Smallest and largest for arr2:", second_smallest_and_largest(arr2))
