#!/usr/bin/env python3
'''Encode and Decode Strings:

Design an algorithm to encode a list of strings to a single string. The encoded
string is then decoded back to the original list of strings.

Please implement encode and decode

Example 1:
Input: ["neet","code","love","you"]
Output:["neet","code","love","you"]

Example 2:
Input: ["we","say",":","yes"]
Output: ["we","say",":","yes"]

Constraints:
0 <= strs.length < 100
0 <= strs[i].length < 200
strs[i] contains only UTF-8 characters.


Recommended Time & Space Complexity:

You should aim for a solution with O(m) time for each encode() and decode() call
and O(m+n) space, where m is the sum of lengths of all the strings and n is the
number of strings.


My plan is to use some special string character as a delimiter, but I have to
choose something that won't occur in my samples and/or sanitize my inputs.

Claude suggested a null byte, '\x00', which is a good idea, but first I'm going
to write code for a generic delimiter.

'''

class Solution:
    delimiter = "||"
    exception = "|||"

    def encode(self, strs: list[str]) -> str:
        if not strs:  # checks for empty array
            return self.exception
        else:
            output = self.delimiter.join(strs)
            return output

    def decode(self, s: str) -> list[str]:
        if s == self.exception:
            return []
        else:
            return s.split(self.delimiter)

# strs = ["neet","code","love","you"]  # Output:["neet","code","love","you"]
# strs = ["we","say",":","yes"]  # Output: ["we","say",":","yes"]
# strs = []  # Output: []
# strs = [""]  # Output: [""]
# strs = ["", ""]
strs = ["", "", ""]

solution = Solution()

print(f"Input is {strs}")

encoded = solution.encode(strs)
print(f"Encoded: {encoded}, which is type {type(encoded)}")

decoded = solution.decode(encoded)
print(f"Decoded: {decoded}")

print(f"Satisfactory: {strs == decoded}")
