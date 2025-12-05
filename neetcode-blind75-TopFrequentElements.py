#!/usr/bin/env python3
'''Top K Frequent Elements

Given an integer array 'nums' and an integer 'k', return the 'k' most frequent
elements within the array.

The test cases are generated such that the answer is always unique.

You may return the output in any order.

Example 1:
Input: nums = [1,2,2,3,3,3], k = 2
Output: [2,3]

Example 2:
Input: nums = [7,7], k = 1
Output: [7]

Constraints:
1 <= nums.length <= 10^4.
-1000 <= nums[i] <= 1000
1 <= k <= number of distinct elements in nums.


This actually works as basically a one-liner for the body:
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        return [num for num, count in Counter(nums).most_common(k)]
'''
from collections import Counter

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # Create dictionary with num:count as key:value,
        # sorted by descending value
        tallyDict: dict = Counter(nums)

        # Extract 'k' elements from tallyDict with highest values
        topTallyPairs: list[tuple[int]] = tallyDict.most_common(k)

        # Return a list with only the key values, i.e. the first element of
        # each sub-list
        topTallyElements: list[int] = [sublist[0] for sublist in topTallyPairs]
        return topTallyElements


nums = [1,2,3,2,3,3,3,4]; k = 2
# Output: [2,3]

# nums = [7,7]; k = 1
# Output: [7]

solution = Solution()
result = solution.topKFrequent(nums, k)
print("The final result is:")
print(result)
