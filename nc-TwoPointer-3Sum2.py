#!/usr/bin/env python3
'''3Sum

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all
distinct.

The output should not contain any duplicate triplets. You may return the output
and the triplets in any order.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].

Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

Constraints:
3 <= nums.length <= 1000
-10^5 <= nums[i] <= 10^5

Recommended Time & Space Complexity
You should aim for a solution with O(n^2) time and O(1) space, where n is the
size of the input array.


Notes:

Well my first attempt turned into a mess, so I thought about it while I was
going to bed last night and put it together: loop through the list, and at each
loop you use double-pointers on the rest of the list.

Woof. Even once I knew the pattern that took waaay too long to work out all the
details of

'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []
        
        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                triplet = [nums[i], nums[left], nums[right]]
                total = nums[i] + nums[left] + nums[right]
                
                # print([i, left, right], triplet, total, results)

                if total == 0:
                    results.append(triplet)

                    # Skip duplicates for second element
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # Skip duplicates for third element
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1
                elif total > 0:
                    right -= 1
                else:
                    left += 1

        return results


# nums = [-1,0,1,2,-1,-4]  # Output: [[-1,-1,2],[-1,0,1]]
# nums = [-4,-1,-1,0,1,2]  # Output: [[-1,-1,2],[-1,0,1]]
# nums = [0,1,1]  # Output: []
nums = [0,0,0]  # Output: [[0,0,0]]
# nums = [0, 0, 0, 0]  # Output: [[0,0,0]]
# nums = [-1, 0, 1, 0]  # Output [[-1,0,1]]
# nums = [-2,0,1,1,2]  # [[-2,0,2],[-2,1,1]]
# nums = [34,55,79,28,46,33,2,48,31,-3,84,71,52,-3,93,15,21,-43,57,-6,86,56,94,74,83,-14,28,-66,46,-49,62,-11,43,65,77,12,47,61,26,1,13,29,55,-82,76,26,15,-29,36,-29,10,-70,69,17,49]
# Output = [[-82,-11,93],[-82,13,69],[-82,17,65],[-82,21,61],[-82,26,56],[-82,33,49],[-82,34,48],[-82,36,46],[-70,-14,84],[-70,-6,76],[-70,1,69],[-70,13,57],[-70,15,55],[-70,21,49],[-70,34,36],[-66,-11,77],[-66,-3,69],[-66,1,65],[-66,10,56],[-66,17,49],[-49,-6,55],[-49,-3,52],[-49,1,48],[-49,2,47],[-49,13,36],[-49,15,34],[-49,21,28],[-43,-14,57],[-43,-6,49],[-43,-3,46],[-43,10,33],[-43,12,31],[-43,15,28],[-43,17,26],[-29,-14,43],[-29,1,28],[-29,12,17],[-14,-3,17],[-14,1,13],[-14,2,12],[-11,-6,17],[-11,1,10],[-3,1,2]]

solution = Solution()
result = solution.threeSum(nums)
print("The final result is:")
print(result)
