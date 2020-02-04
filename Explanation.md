## Problem 1
Time Complexity ~ Is O(log(n)) Using binary search algorithm to find the square root of
The number so every time the number of steps reduced to half the number of total Steps
Space complexity is O(1) ~ Space complexity is Constant O(1)

Code analysis~ Using the binary search algorithm I am trying to find the square root of the number in this problem.
If the square is between the mid and (mid + 1), then mid is returned as the floored square root.


## Problem 2
The main step is to find the pivot and then search for the element afterwards
We are using Binary search to find the pivot index and then
applying the binary serach again to find the target
Time Complexity ~ O(logn)
Space Complexity ~ O(1)

Code Analysis~
This problem requires to find given number in an array. So th Binary search algorithm
fits for this problem to find given number from the array as the array is sorted but for this
problem, I need to search for number in rotated array. So in order to achieve the required solution
I need to find pivot point from where the array is rotated and after that I can implement
Binary Search and that is what I have done for this problem.

## Problem 3
Time Complexity ~
Since we are doing Bubble sort so the time complexity for that
is O(logn) and we are doing for n such
elements so the overall time complexity is O(nlogn)
Space Complexity~ O(n)

Code Analysis~
For this problem I am sorting the array in decreasing order using Bibble sort algorithm
Then iterating through the list to find for two number whose sum is Maximum among all the numbers in that list.
In rearrangedigits first time we iterate in the list and increament is by 2  to get the digits alternatively
and we keep on adding to the base of 10 to get the largest possible number and did the same for the to find the second largest number.

## Problem 4
Time Complexity ~
O(n) since we are iterating over the n elements

Space Complexity~
O(1) Constant

Code Analysis~
Simply applying sorting technique which is in place and return the list.


## Problem 5
TrieNode's time complexity and space complexity to insert a character is O(1).
TrieNode's time complexity and space complexity of suffixes of a node is O(M*N).

Trie's time complexity and space complexity to insert a word is O(n).
Trie's time complexity to find a prefix is O(n) and space complexity is O(1).

Code Analysis ~ In this problem I have implemented Trie structure that is similar to Tree structure
to store dynamic set of strings. Using class TrieNode and its methods insert and suffixes I
am using Trie class to solve the problem.


##Problem 6
Time Complexity ~ Clearly we are iterating over nums in get_min_max and if the size of input is n
then the time complexity is O(n)

Space Complexity is O(1) constant since we are are storing at a specific index in our list in get_min_max function
and in order to that it will consume constant amount of time.

Code Analysis ~ Sorting the list in place sorting algorithm in O(n) time and then simply
returning the first and last element of the list

##Problem 7

 Code analysis ~ In order to implement HTTPRouter using Trie, first I have initialized a RouteTrieNode with value and
 handler as reference to next node and than I have utilized the root node to implement RouteTrie.

RouteTrieNode's time complexity and space complexity both are O(M*N)
RouteTrie's time complexity and space complexity both for lookup and add handler is O(n).