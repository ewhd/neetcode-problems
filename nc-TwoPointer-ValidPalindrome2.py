#!/usr/bin/env python3
'''Valid Palindrome

Given a string s, return true if it is a palindrome, otherwise return false.

A palindrome is a string that reads the same forward and backward. It is also
case-insensitive and ignores all non-alphanumeric characters.

Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).

Example 1:
Input: s = "Was it a car or a cat I saw?"
Output: true
Explanation: After considering only alphanumerical characters we have
"wasitacaroracatisaw", which is a palindrome.

Example 2:
Input: s = "tab a cat"
Output: false
Explanation: "tabacat" is not a palindrome.

Constraints:
1 <= s.length <= 1000
s is made up of only printable ASCII characters.


Recommended Time & Space Complexity
You should aim for a solution with O(n) time and O(1) space, where n is the
length of the input string.


Notes:

This time I need to reach O(1) space requirements, which means I need to operate
on the list as is and without creating any copies.

'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            # skip non-alphanumeric characters
            print("start of while:  ", left, s[left], right, s[right])
            while left < right and not s[left].isalnum():
                left += 1
                print("increment left: ", left)
            while left < right and not s[right].isalnum():
                right -= 1
                print("increment right: ", right)
            print("mid while while: ", left, s[left], right, s[right])
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True


# s = "Was it a car or a cat I saw?"  # Output: true
# s = "tab a cat"  # Output: false
s = ".,"  # Output: true

solution = Solution()
result = solution.isPalindrome(s)
print("The final result is:")
print(result)
