'''
 Rearrange Array Elements so as to form two number such that their sum is maximum.
 Return these two numbers. You can assume that all array elements are in the range [0, 9].
 The number of digits in both the numbers cannot differ by more than 1. You're not allowed
 to use any sorting function that Python provides and the expected time complexity is O(nlog(n)).

for e.g. [1, 2, 3, 4, 5]
he expected answer would be [531, 42].
Another expected answer can be [542, 31].
 In scenarios such as these when there are more than one possible answers, return any one.
'''
def bubble_sort_1(l):
    for iteration in range(len(l)):
        for index in range(1, len(l)):

            this = l[index]
            prev = l[index-1]
            if prev >= this:
                continue

            l[index] = prev
            l[index - 1] = this
    return l

def rearrange_digits(input_list):
    # Sorting the list in descending order
    myList = bubble_sort_1(input_list)
    print(myList)
    x = 0
    i = 0
    while i < len(myList):
        x = x * 10 +  myList[i]
        i += 2

    y = 0
    j = 1
    while j < len(myList):
        y = y * 10 + myList[j]
        j += 2
    print(x , y)
    return [x,y]

def test_function(test_case):
    output   = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")

    else:
        print("Fail")

# Test Cases
test_case_0 = [[1, 2, 3, 4, 5], [542, 31]]
test_function(test_case_0)

test_case_1 = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_function(test_case_1)

test_case_2 = [[],[]]
test_function(test_case_2)

test_case_3 = [[1,0] , [1 , 0]]
test_function(test_case_3)

