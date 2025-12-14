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

My first thoughts on this were all wrong because I was still thinking pairs and
not triplets.

My first thought is for each number, pair it with each remaining number in the
list, then look through the remaining numbers for the difference between that
sum and zero.

So the first triplet check will be the first three numbers:
For [-1,0,1,2,-1,-4]:
1 triplet: -1, 0, 1
2 triplet: -1, 0, 2
3 triplet: -1, 0, -1
4 triplet: -1, 0, -4
5 triplet: -1, 1, 2
6 triplet: -1, 1, -1
7 triplet: -1, 1, -4

REMEMBER! We're looking for *unique* combinations of numbers, not indexes!

I think I might need to use some recursion

'''

class Solution:
    def findTriplet(self, nums: list[int], tripletList: list[int]) -> list[int]:
        '''Find the all pairs of two elements of a list[1:] which when summed
        with list[0] == 0. Return a list of all such triplets

        '''
        first, second, third = 0, 1, 2
        while third < len(nums):
            triplet = [nums[first], nums[second], nums[third]]
            print(first, second, third, [nums[first], nums[second], nums[third]], tripletList, triplet in tripletList)

            if sum(triplet) == 0 and triplet not in tripletList:
                tripletList.append(triplet)

            if third == len(nums) - 1:
                print(first, second, third)

                second += 1
                third = second + 1

            third += 1

        if first < len(nums) - 3:
            tripletList = self.findTriplet(nums[1:], tripletList)
        return tripletList


    def threeSum(self, nums: list[int]) -> list[List[int]]:
        nums.sort()
        # tripletList: list[list[int]] = []

        tripletList = self.findTriplet(nums, [])

        return tripletList

# nums = [-1,0,1,2,-1,-4]  # Output: [[-1,-1,2],[-1,0,1]]
nums = [-4,-1,-1,0,1,2]  # Output: [[-1,-1,2],[-1,0,1]]
# nums = [0,1,1]  # Output: []
# nums = [0,0,0]  # Output: [[0,0,0]]
# nums = [0, 0, 0, 0]  # Output: [[0,0,0]]
# nums = [-1, 0, 1, 0]  # Output [[-1,0,1]]

solution = Solution()
result = solution.threeSum(nums)
print("The final result is:")
print(result)
