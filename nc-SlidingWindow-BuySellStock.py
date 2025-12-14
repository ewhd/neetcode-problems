#!/usr/bin/env python3
'''Best Time to Buy and Sell Stock

You are given an integer array 'prices' where prices[i] is the price of NeetCoin
on the ith day.

You may choose a single day to buy one NeetCoin and choose a different day in
the future to sell it.

Return the maximum profit you can achieve. You may choose to not make any
transactions, in which case the profit would be 0.

Example 1:
Input: prices = [10,1,5,6,7,1]
Output: 6
Explanation: Buy prices[1] and sell prices[4], profit = 7 - 1 = 6.

Example 2:
Input: prices = [10,8,7,5,2]
Output: 0
Explanation: No profitable transactions can be made, thus the max profit is 0.

Constraints:

1 <= prices.length <= 100
0 <= prices[i] <= 100


Recommended Time & Space Complexity:
You should aim for a solution with O(n) time and O(1) space, where n is the size
of the input array.


Notes:

Sliding window means you're somehow holding a subset, then subtracting the
lowest index value and adding the next to move the window along. This allows you
to move the subset through the array without performing nested loops, thereby
keeping the time-complexity low.

For this problem, we need to keep track of the lowest and the highest values
that we've seen.
Ah, but there's a catch. Imagine this array: [4, 10, 1, 8]. 
Ah, the sliding window can have a variable length!

So, we have left and right values, which start with prices[0] and prices[1], and
we have a highestProfit variable, in which we'll store the largest diffProfit of left
and right which we have yet encountered.
If the right value is larger than the left:
    if diffProfit of left + right > highestProfit: highestProfit = diffProfit
    advance right index by 1
if the left value is larger than the right:
    set left to right
    advance right by 1

'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit: int = 0
        leftIndex: int = 0
        rightIndex: int = 1

        while rightIndex < len(prices):
            if prices[rightIndex] < prices[leftIndex]:
                leftIndex = rightIndex
            else:
                maxProfit = max(maxProfit, prices[rightIndex] - prices[leftIndex])
            rightIndex += 1

        return maxProfit
                
            
        

prices = [10,1,5,6,7,1]  # Output: 6
# prices = [10,8,7,5,2]  # Output: 0


solution = Solution()
result = solution.maxProfit(prices)
print("The final result is:")
print(result)
