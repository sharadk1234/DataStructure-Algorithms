'''
 Given an input ``array consisting on only 0, 1, and 2,
 sort the array in a single traversal.
 You're not allowed to use any sorting function that Python provides.
'''
def sort_012(nums):
    for i in range(len(nums)):
        _min = min(nums[i:])
        min_index = nums[i:].index(_min)
        nums[i + min_index] = nums[i]
        nums[i] = _min
    return nums

def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print('Pass')
    else:
        print('Fail')

# Test Cases
test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
test_function([])
test_function([0,0,0,0,0])


