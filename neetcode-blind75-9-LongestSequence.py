#!/usr/bin/env python3
'''Longest Consecutive Sequence

Given an array of integers nums, return the length of the longest consecutive
sequence of elements that can be formed.

A consecutive sequence is a sequence of elements in which each element is
exactly 1 greater than the previous element. The elements do not have to be
consecutive in the original array.

You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [2,20,4,10,3,4,5]
Output: 4
Explanation: The longest consecutive sequence is [2, 3, 4, 5].

Example 2:
Input: nums = [0,3,2,5,4,6,1,1]
Output: 7

Constraints:
0 <= nums.length <= 1000
-10^9 <= nums[i] <= 10^9


Recommended Time & Space Complexity You should aim for a solution as good or
better than O(n) time and O(n) space, where n is the size of the input array.


Notes:

sort list
loop through list, compairing steps between consecutive pairs
use a counter to count up each time step is 1, reset if not 1
- repeats don't count, so check for difference of 1 or 0

Oh right, resetting the counter isn't right. I might have multiple consecutive
runs, and I want the longest, so I need to save that run when it's finished.

'''

from itertools import pairwise


class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums.sort()  # sort list in place
        print(nums)
        # consecutiveCounter: int = 1
        allRuns: list = [1]
        for (first, second) in pairwise(nums):
            difference = second - first
            print(f"{(first, second)}, {difference}, {allRuns}")
            if difference == 0:
                # consecutiveCounter = consecutiveCounter
                pass
            elif difference == 1:
                # consecutiveCounter += 1
                allRuns[1] += 1
            elif difference > 1:
                allRuns.append(allRuns[1])
                allRuns[1] = 1
                
                # consecutiveCounter = 1
            
        print(allRuns)
        return allRuns


# nums = [2,20,4,10,3,4,5]  # Output: 4
nums = [0,3,2,5,4,6,1,1]  # Output: 7

solution = Solution()
result = solution.longestConsecutive(nums)
print("The final result is:")
print(result)
