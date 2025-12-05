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


Previous attempts had time complexity = O(n + k log n) where n = len(nums),
because Counter is O(n) and most_common uses heap

This time I'm trying to reduce time complexity to O(n), using "bucket sort"
'''
from collections import Counter

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # Create dictionary with num:count as key:value,
        # sorted by descending value
        tallyDict: dict = Counter(nums)

        # Create buckets where bucket[i] = numbers with frequency i
        # O(n) space, O(n) time
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in tallyDict.items():
            buckets[freq].append(num)

        # Return list of top 'k' elements with highest frequencies
        results: list = []
        for frequency in range(len(nums) -1, 0, -1):
            results.extend(buckets[frequency])
        return results[:k]


nums = [1,2,3,2,3,3,3,4]; k = 2
# Output: [2,3]

# nums = [7,7]; k = 1
# Output: [7]

solution = Solution()
result = solution.topKFrequent(nums, k)
print("The final result is:")
print(result)
