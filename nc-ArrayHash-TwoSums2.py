from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        for index, num in enumerate(nums):
            complement = target - num
            if complement in numMap:
                return [numMap[complement], index]
            numMap[num] = index
        return []
                
# Example usage
solution = Solution()
# nums = [1, 2, 3, 4, 5]; target = 8 # [2, 4]
# nums=[3,4,5,6]; target=7           # [0, 1]
# nums=[-1,-2,-3,-4,-5]; target=-8   # [2, 4]
# nums=[-10,-1,-18,-19]; target=-19  # [1, 2]
nums=[3, 2, 3]; target=6           # [0, 2]

result = solution.twoSum(nums, target)
print("The final result is " + str(result))
