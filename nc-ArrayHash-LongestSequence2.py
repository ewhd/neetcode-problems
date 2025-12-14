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

My first try relied on sort(), which is O(n log n), not O(n).

Claude suggests using a hash set (see below)

A hash set 

Apparently in python sets are actually constructed as hash sets behind the
scenes

'''

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if nums == []:
            return 0

        print(nums)
        numSet = set(nums)
        print(numSet)
        maxLength = 1

        for num in numSet:
            if num -1 not in numSet:
                currentNum = num
                currentLength =1
                print(num, num -1, currentNum, currentLength)

                while currentNum + 1 in numSet:
                    currentNum += 1
                    currentLength += 1
                    print(currentNum, currentLength)
                maxLength = max(maxLength, currentLength)
                print(maxLength)
        return maxLength




# nums = [2,20,4,10,3,4,5]  # Output: 4
# nums = [0,3,2,5,4,6,1,1]  # Output: 7
nums = []  # Output: 0

solution = Solution()
result = solution.longestConsecutive(nums)
print("The final result is:")
print(result)
