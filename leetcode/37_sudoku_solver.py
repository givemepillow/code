from typing import List


class Solution:
    items = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        return self.solve(board)

    def solve(self, board: List[List[str]]) -> List[List[str]]:
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    available = self.available_items(i, j, board)
                    for number in available:
                        board[i][j] = number
                        next_board = self.solve(board)
                        if next_board:
                            return next_board
                        else:
                            board[i][j] = '.'
                    return False
        return board

    def available_items(self, row: int, column: int, board: List[List[str]]):
        available = self.items.copy()
        right, bottom = row // 3, column // 3
        row_items = set(board[row])
        column_items = set([board[i][column] for i in range(len(board))])
        square_items = set([board[i + (right * 3)][j + (bottom * 3)] for i in range(3) for j in range(3)])
        available = available - (square_items | row_items | column_items)
        return available


solution = Solution()
# print(solution.solveSudoku(
#     [
#         ["5", "3", ".", ".", "7", ".", ".", ".", "."],
#         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
#         [".", "9", "8", ".", ".", ".", ".", "6", "."],
#         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
#         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
#         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
#         [".", "6", ".", ".", ".", ".", "2", "8", "."],
#         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
#         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
# ))
#
# print(solution.solveSudoku(
#     [[".", ".", "9", "7", "4", "8", ".", ".", "."],
#      ["7", ".", ".", ".", ".", ".", ".", ".", "."],
#      [".", "2", ".", "1", ".", "9", ".", ".", "."],
#      [".", ".", "7", ".", ".", ".", "2", "4", "."],
#      [".", "6", "4", ".", "1", ".", "5", "9", "."],
#      [".", "9", "8", ".", ".", ".", "3", ".", "."],
#      [".", ".", ".", "8", ".", "3", ".", "2", "."],
#      [".", ".", ".", ".", ".", ".", ".", ".", "6"],
#      [".", ".", ".", "2", "7", "5", "9", ".", "."]]
# ))

print(solution.solveSudoku(
    [[".", ".", ".", "2", ".", ".", ".", "6", "3"],
     ["3", ".", ".", ".", ".", "5", "4", ".", "1"],
     [".", ".", "1", ".", ".", "3", "9", "8", "."],
     [".", ".", ".", ".", ".", ".", ".", "9", "."],
     [".", ".", ".", "5", "3", "8", ".", ".", "."],
     [".", "3", ".", ".", ".", ".", ".", ".", "."],
     [".", "2", "6", "3", ".", ".", "5", ".", "."],
     ["5", ".", "3", "7", ".", ".", ".", ".", "8"],
     ["4", "7", ".", ".", ".", "1", ".", ".", "."]]
))
