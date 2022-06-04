from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        uniques = set()
        for row in board:
            uniques.clear()
            for value in row:
                if value == '.':
                    continue
                elif value in uniques:
                    return False
                else:
                    uniques.add(value)
        for i in range(9):
            uniques.clear()
            for j in range(9):
                value = board[j][i]
                if value == '.':
                    continue
                elif value in uniques:
                    return False
                else:
                    uniques.add(value)

        for right_shift in range(0, 7, 3):
            for bottom_shift in range(0, 7, 3):
                uniques.clear()
                for i in range(0, 3):
                    for j in range(0, 3):
                        value = board[bottom_shift + i][right_shift + j]
                        if value == '.':
                            continue
                        elif value in uniques:
                            return False
                        else:
                            uniques.add(value)
        return True


solution = Solution()
print(solution.isValidSudoku(
    [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."]
        , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
        , [".", "9", "8", ".", ".", ".", ".", "6", "."]
        , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
        , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
        , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
        , [".", "6", ".", ".", ".", ".", "2", "8", "."]
        , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
        , [".", ".", ".", ".", "8", ".", "7", "1", "9"]
    ]
))

print(solution.isValidSudoku(
    [[".", ".", "4", ".", ".", ".", "6", "3", "."],
     [".", ".", ".", ".", ".", ".", ".", ".", "."],
     ["5", ".", ".", ".", ".", ".", ".", "9", "."],
     [".", ".", ".", "5", "6", ".", ".", ".", "."],
     ["4", ".", "3", ".", ".", ".", ".", ".", "1"],
     [".", ".", ".", "7", ".", ".", ".", ".", "."],
     [".", ".", ".", "5", ".", ".", ".", ".", "."],
     [".", ".", ".", ".", ".", ".", ".", ".", "."],
     [".", ".", ".", ".", ".", ".", ".", ".", "."]]
))
