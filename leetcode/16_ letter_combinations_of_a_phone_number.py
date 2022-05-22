from typing import List


class Solution:
    letters = {
        '1': "",
        '2': "abc",
        '3': "def",
        '4': "ghi",
        '5': "jkl",
        '6': "mno",
        '7': "pqrs",
        '8': "tuv",
        '9': "wxyz"
    }

    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        stack = []

        def dfs(_digits: str):
            if not _digits:
                result.append("".join(stack))
            else:
                for char in self.letters[_digits[0]]:
                    stack.append(char)
                    dfs(_digits[1:])
                    stack.pop()

        if digits:
            dfs(digits)
        return result


solution = Solution()
print(solution.letterCombinations('22'))
