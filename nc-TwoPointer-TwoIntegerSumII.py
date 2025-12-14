#!/usr/bin/env python3
'''Two Integer Sum II

Given an array of integers numbers that is sorted in non-decreasing order.

Return the indices (1-indexed) of two numbers, [index1, index2], such that they
add up to a given target number target and index1 < index2. Note that index1 and
index2 cannot be equal, therefore you may not use the same element twice.

There will always be exactly one valid solution.

Your solution must use O(1) additional space.

Example 1:
Input: numbers = [1,2,3,4], target = 3
Output: [1,2]
Explanation: The sum of 1 and 2 is 3. Since we are assuming a 1-indexed array,
index1 = 1, index2 = 2. We return [1, 2].

Constraints:
2 <= numbers.length <= 1000
-1000 <= numbers[i] <= 1000
-1000 <= target <= 1000

Recommended Time & Space Complexity:
You should aim for a solution with O(n) time and O(1) space, where n is the
size of the input array.


Notes:



'''

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left, right = 0, len(numbers) -1
        while left < right:
            sum = numbers[left] + numbers[right]
            if sum == target:
                return [left + 1, right + 1]
            elif sum > target:
                right -= 1
            elif sum < target:
                left += 1

# numbers = [1,2,3,4]; target = 3  # Output: [1,2]
numbers = [2,3,4]; target = 6  # Output: [1,3]

solution = Solution()
result = solution.twoSum(numbers, target)
print("The final result is:")
print(result)
