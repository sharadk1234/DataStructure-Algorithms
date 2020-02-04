'''
You are given a sorted array which is rotated at some random pivot point.
Example: [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]
You are given a target value to search. If found in the array return its
index, otherwise return -1.
You can assume there are no duplicates in the array and your
algorithm's runtime complexity must be in the order of O(log n).
'''


'''
Our Approach: Binary search to find index of pivot (where the array has been rotated).
Normal Binary search on both sides of pivot to find element
Code uses the property that the last element of array will be smaller than all elements before the pivot.
example: in rotated array: [8,9,11,5,6,7] We know 5 is the pivot.
All elements on left side of pivot are larger than last element, 7
All elements on right side of pivot including pivot are smaller than last element, 7.
'''

def rotated_array_search(input_list, target):
   if (not input_list):
       return -1
   pivot_index = find_pivot(input_list)
   result = bin_search(input_list,target, 0 ,pivot_index - 1)
   if (result != -1):
       return result
   else:
       return bin_search(input_list, target,pivot_index,len(input_list) -1)

def find_pivot(arr):
    # Compare last element to mid element
    # Compare last element to mid element
    # If the md element is greater than the last element which means -> pivot must be on right
    # Move right move mid + 1
    # If mid element is less than last element, move the high to mid - 1
    element_to_compare = arr[-1]
    low = 0
    high = len(arr) - 1
    while (low <= high):
        mid = (low + high) // 2
        if element_to_compare < arr[mid]:
            low = mid + 1 # moving pivot to the right side of the array
        elif element_to_compare >= arr[mid]:
            high = mid -1 # moving the pivot the left side of the array
    return low

def bin_search(arr,target,low,high):
    while low <= high:
        mid = (low + high) // 2
        if target < arr[mid]:
            high = mid - 1 # search in the left sub half
        elif target > arr[mid]:
            low = mid + 1
        else:
            return mid
    return -1

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

# Test Cases and edge cases
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
test_function(([[], 1]))
test_function([[1,2,3,4,5], -1])