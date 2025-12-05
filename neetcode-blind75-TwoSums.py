#!/usr/bin/env python3

# Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

# You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

# Return the answer with the smaller index first.

## Example 1:
# Input:   nums = [3,4,5,6], target = 7
# Output:  [0,1]
# Explanation: nums[0] + nums[1] == 7, so we return [0, 1].

## Example 2:
# Input:   nums = [4,5,6], target = 10
# Output:  [0,2]

## Example 3:
# Input:   nums = [5,5], target = 10
# Output:  [0,1]

## Constraints:
# 2 <= nums.length <= 1000
# -10,000,000 <= nums[i] <= 10,000,000
# -10,000,000 <= target <= 10,000,000

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         def create_mapping(nums: List[int]):
#             indexed_nums = list(enumerate(nums))
#             sorted_indexed_nums = sorted(indexed_nums, key=lambda x: x[1])
#             index_mapping = {i: original_index for i, (original_index, value) in enumerate(sorted_indexed_nums)}
#             return index_mapping

#         indexMap = create_mapping(nums)
#         nums.sort()
#         lowIndex = 0
#         highIndex  = len(nums) -1
#         while True:
#             sum = nums[lowIndex] + nums[highIndex]
#             print([lowIndex, highIndex], sum)
#             if lowIndex >= highIndex:
#                 print("An error has occurred")
#                 return None
#             elif sum  == target:
                
#                 return [indexMap[lowIndex], indexMap[highIndex]]
#             elif abs(sum) > abs(target):
#                 highIndex -=1
#                 continue
#             elif abs(sum) < abs(target):
#                 lowIndex += 1
#                 continue

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        def checkRestOfList (nums: List[int], lowIndex):
            print(nums, lowIndex)
            if len(nums) < 2:
                return None
            
            lowIndexVal = nums.pop(0)
            for highIndex in range(len(nums)):
                sum = lowIndexVal + nums[highIndex]
                print([lowIndex, highIndex + lowIndex + 1], sum)
                
                if sum == target:
                    highIndex = highIndex + lowIndex + 1
                    print("highIndex = " + str(highIndex))
                    print("lowIndex = " + str(lowIndex))
                    return [lowIndex, highIndex]
 
            result = checkRestOfList(nums, lowIndex +1)
            # return nums, lowIndex
            return result

        pair = checkRestOfList(nums, 0)
        print(pair)
        return pair or []
                
            
                
solution = Solution()

# Call the twoSum method
# nums = [1, 2, 3, 4, 5]
# target = 8

# nums=[3,4,5,6]
# target=7

nums=[-1,-2,-3,-4,-5]
target=-8

# nums=[-10,-1,-18,-19]
# target=-19

# nums=[3, 2, 3]
# target=6

result = solution.twoSum(nums, target)
print("The final result is " + str(result))
