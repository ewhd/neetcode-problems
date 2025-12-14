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

this feels like it should be easy...
strip non alphanumeric characters, compare to the reverse. right?

That won't be efficient enough. We're aiming for O(1) space, which I think means
we have to work on the string in place and create create a second one, even
while stripping out characters.

So the below works, but is O(n) because it creates a new string
(alphaNumOnlyString)

'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphaNumOnlyString: str = ''.join(char for char in s if char.isalnum()).lower()
        print(alphaNumOnlyString)

        left, right = 0, len(alphaNumOnlyString) - 1
        while left < right:
            if alphaNumOnlyString[left] != alphaNumOnlyString[right]:
                return False
            left += 1
            right -= 1
        return True


# s = "Was it a car or a cat I saw?"  # Output: true
s = "tab a cat"  #Output: false

solution = Solution()
result = solution.isPalindrome(s)
print("The final result is:")
print(result)
