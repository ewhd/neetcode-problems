#!/usr/bin/env python3
'''Valid Sudoku

You are given a 9 x 9 Sudoku board board. A Sudoku board is valid if the
following rules are followed:

Each row must contain the digits 1-9 without duplicates. Each column must
contain the digits 1-9 without duplicates. Each of the nine 3 x 3 sub-boxes of
the grid must contain the digits 1-9 without duplicates. Return true if the
Sudoku board is valid, otherwise return false

Note: A board does not need to be full or be solvable to be valid.

Example 1:
Input: board = 
[["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]
Output: true


Example 2:
Input: board = 
[["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","1",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: There are two 1's in the top-left 3x3 sub-box.

Constraints:
board.length == 9
board[i].length == 9
board[i][j] is a digit 1-9 or '.'.

Recommended Time & Space Complexity: You should aim for a solution as good or
better than O(n^2) time and O(n^2) space, where n is the number of rows in the
square grid.


Notes:

So this is all about identifying if the board contains patterns that are not
valid, which is something I do at a glance irl. So how do I do that?

Well I look for doubles, i.e. check for uniqueness, in each row, column, and
block.

I think I want to create a new list with sublists of each row/column/block, so
27 total sublists. Then I can iterate through and strip empty squares

row is easy, cause each row is its own list
for row in board:
    copy row
    append copied row to accumulator list

columns are also pretty simple, since it's the same index from each row
for column in range(9):
    open an empty list
    for row in board:
       add row[column] to list
    append this list to accumulator

I could probably do something similar but more complicated for the blocks
block 1: row 1-3, col 1-3
block 2: row 1-3, col 4-6
block 3: row 1-3, col 7-9
block 4: row 4-6, col 1-3
block 5: row 4-6, col 4-6
block 6: row 4-6, col 7-9
block 7: row 7-9, col 1-3
block 8: row 7-9, col 4-6
block 9: row 7-9, col 7-9




once I can reference each sub-unit, then I'll check validity by checking for
uniqueness within each unit (ignoring empty squares)

check uniqueness: len(list) == len(set(list))

'''

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        

board = 
[["1","2",".", ".","3",".", ".",".","."],
 ["4",".",".", "5",".",".", ".",".","."],
 [".","9","8", ".",".",".", ".",".","3"],
 
 ["5",".",".", ".","6",".", ".",".","4"],
 [".",".",".", "8",".","3", ".",".","5"],
 ["7",".",".", ".","2",".", ".",".","6"],
 
 [".",".",".", ".",".",".", "2",".","."],
 [".",".",".", "4","1","9", ".",".","8"],
 [".",".",".", ".","8",".", ".","7","9"]]
# Output: true

# board = 
# [["1","2",".",".","3",".",".",".","."],
#  ["4",".",".","5",".",".",".",".","."],
#  [".","9","1",".",".",".",".",".","3"],
#  ["5",".",".",".","6",".",".",".","4"],
#  [".",".",".","8",".","3",".",".","5"],
#  ["7",".",".",".","2",".",".",".","6"],
#  [".",".",".",".",".",".","2",".","."],
#  [".",".",".","4","1","9",".",".","8"],
#  [".",".",".",".","8",".",".","7","9"]]
# Output: false

solution = Solution()
result = solution.isValidSudoku(board)
print("The final result is:")
print(result)
