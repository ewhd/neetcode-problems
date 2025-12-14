#!/usr/bin/env python3
'''Container With Most Water

You are given an integer array 'heights' where heights[i] represents the height
of the i-th bar.

You may choose any two bars to form a container. Return the maximum amount of water a container can store.

Example 1:
Input: height = [1,7,2,5,4,7,3,6]
Output: 36

Example 2:
Input: height = [2,2,2]
Output: 4

Constraints:
2 <= height.length <= 1000
0 <= height[i] <= 1000

Recommended Time & Space Complexity
You should aim for a solution with O(n) time and O(1) space, where n is the
size of the input array.


Notes:

So, any to elements, find the area by:
        (height)         *           (width)
(larger of the elements) * (difference of the two indexes)

'''
# import time

class Solution:
    def maxArea(self, heights: list[int]) -> int:
        left = 0
        right = len(heights) -1

        maxArea = 0
        while left < right:
            height = min(heights[left], heights[right])
            width = right - left
            area = height * width

            maxArea = max(maxArea, area)

            print([left, right],
                  [heights[left], heights[right]],
                  height,
                  width,
                  area,
                  maxArea)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return maxArea


# heights = [1,7,2,5,4,7,3,6]  # Output: 36
heights = [2,2,2]  # Output: 4

solution = Solution()
result = solution.maxArea(heights)
print("The final result is:")
print(result)
