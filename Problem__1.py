# Finding the Square Root of an Integer
# Find the square root of the integer without
# Using any Python library. You have to find the floor value of the square root.
# The expected time complexity is O(log(n))
# Binary Search Approach Time complexity is O(logn)

def sqrt(x):
    # If a number is less than 0 Than It's sqaure root is not possible
    if x < 0:
        print('Complex Number')
        return
    left = 0
    right = x

    while left <= right:
        middle = (left + right) // 2
        if middle**2 == x:
            return middle
        if middle**2 < x:
            left = middle + 1
        else:
            right = middle - 1
    return right

#Another Approach ~ Newton's Methos
def sqrt_(number):
    root = number
    while root**2 > number:
        root = (root**2 + number)//(2 * root)
    return root

r = sqrt(27)
print(r)
print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")
print ("Pass" if  (10 == sqrt(100)) else "Fail")
#Edge Cases ~
root_1 = sqrt(-1)   # Square root of negative number is Complex number
print(root_1)