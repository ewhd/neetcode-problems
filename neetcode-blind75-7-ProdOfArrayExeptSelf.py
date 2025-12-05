#!/usr/bin/env python3
'''Products of Array Except Self

Given an integer array nums, return an array output where output[i] is the
product of all the elements of nums except nums[i].

Each product is guaranteed to fit in a 32-bit integer.

Follow-up: Could you solve it in O(n) time without using the division operation?

Example 1:
Input: nums = [1,2,4,6]
Output: [48,24,12,8]

Example 2:
Input: nums = [-1,0,1,2,3]
Output: [0,-6,0,0,0]

Constraints:
2 <= nums.length <= 1000
-20 <= nums[i] <= 20

Recommended Time & Space Complexity You should aim for a solution as good or
better than O(n) time and O(n) space, where n is the size of the input array.


Notes:

Haha, I immediately thought of a way to use division:
- multiply up every member of the array = bigNumber
- make a new array where newArray[n] = bigNumber / nums[n]

So let's go ahead and code that.

Well, that only works without a 0 in the mix, lol.
Negative numbers don't seem to be a problem, though.

Ok I've got a working solution that doesn't use division, but it's O(n^2)
because I call math.prod() twice.

'''

import math

class Solution:
    def prodOfAllOthers(self, nums: list[int], index: int) -> int:
        return math.prod(nums[:(index)]) * math.prod(nums[(index+1):])

    def productExceptSelf(self, nums: list[int]) -> list[int]:
        output: list = []
        for index in range(len(nums)):
            output.append(self.prodOfAllOthers(nums, index))
        return output


# nums = [1,2,4,6]  # Output: [48,24,12,8]
nums = [-1,0,1,2,3]  # Output: [0,-6,0,0,0]

solution = Solution()
result = solution.productExceptSelf(nums)
print("The final result is:")
print(result)
