#!/usr/bin/env python3
'''Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without duplicate
characters.

A substring is a contiguous sequence of characters within a string.

Example 1:
Input: s = "zxyzxyz"
Output: 3
Explanation: The string "xyz" is the longest without duplicate characters.

Example 2:
Input: s = "xxxx"
Output: 1

Constraints:
0 <= s.length <= 1000
s may consist of printable ASCII characters.

Recommended Time & Space Complexity:
You should aim for a solution with O(n) time and O(m) space, where n is the
length of the string and m is the number of unique characters in the string.

'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        

s = "zxyzxyz"  # Output: 3
# s = "xxxx"  # Output: 1

solution = Solution()
result = solution.lengthOfLongestSubstring(s)
print("The final result is:")
print(result)
