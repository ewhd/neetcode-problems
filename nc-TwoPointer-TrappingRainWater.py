#!/usr/bin/env python3
'''Trapping Rain Water

You are given an array of non-negative integers 'height' which represent an
elevation map. Each value height[i] represents the height of a bar, which has a
width of 1.

Return the maximum area of water that can be trapped between the bars.

Example 1:
Input: height = [0,2,0,3,1,0,1,3,2,1]
Output: 9


Constraints:
1 <= height.length <= 1000
0 <= height[i] <= 1000


Recommended Time & Space Complexity
You should aim for a solution as good or better than O(n) time and O(n) space,
where n is the size of the input array.


Notes:

My first thought is something like:
- measure index diff between a value and the highest of remaining values
- find the area of that
- subtract any values between them

Illustration:
|------------------|
|      ██wwwwww██  |
|  ██ww██wwwwww██  |
|__██ww████ww██████|
|0 2 0 3 1 0 1 3 1 |
|0 1 2 3 4 5 6 7 8 |
|------------------|

|------------------------|
|              ██        |
|      ██wwwwww████ww██  |
|__██ww████ww████████████|
|0 1 0 2 1 0 1 3 2 1 2 1 |
|0 1 2 3 4 5 6 7 8 91011 |
|------------------------|

|------------|
|          ██|
|██wwwwwwww██|
|██wwww██ww██|
|████ww██████|
|████ww██████|
|4 2 0 3 2 5 |
|0 1 2 3 4 5 |
|------------|

'''

class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0

        left = 0
        right = len(height) - 1

        leftMax = height[left]
        rightMax = height[right]

        while left < right:
            if leftMax < rightMax:
                left += 1
                leftMax = max(height[left], leftMax)
                total += leftMax - height[left]
            else:
                right -= 1
                rightMax = max(height[right], rightMax)
                total += rightMax - height[right]
    


        return total


# height = [0,2,0,3,1,0,1,3,2,1]  # Output: 9
height=[0,1,0,2,1,0,1,3,2,1,2,1]  # Output: 6
# height=[4,2,0,3,2,5]  # Output: 9

solution = Solution()
result = solution.trap(height)
print("The final result is:")
print(result)
