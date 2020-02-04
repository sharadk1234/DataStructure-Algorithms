'''
In this problem, we will look for smallest and largest integer from a list of unsorted integers.
 The code should run in O(n) time. Do not use Python's inbuilt functions to find min and max.
'''
import random

def get_min_max(nums):
    if nums == []:
        return (None, None)
    for i in range(len(nums)):
        _min = min(nums[i:])
        min_index = nums[i:].index(_min)
        nums[i + min_index] = nums[i]
        nums[i] = _min

    return (nums[0], nums[-1])


# Test Cases
l_0= [i for i in range(0 ,10)]   # A list containing 0 - 9
random.shuffle(l_0) #(0 , 9)
print("Pass" if ((0,9) == get_min_max(l_0)) else "Fail")

l_1 = []    #(None,None)
print("Pass" if ((None,None) == get_min_max(l_1)) else "Fail")

l_2 = [-1,-2,-3,-4,-5]  #(-5,-1)
print("Pass" if ((-5,-1) == get_min_max(l_2)) else "Fail")

l_3 = [-100]            # (-100,100)
print("Pass" if ((-100, -100) == get_min_max(l_3)) else "Fail")
