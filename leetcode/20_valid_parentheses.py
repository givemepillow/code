class Solution:
    parentheses = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in self.parentheses:
                if not stack or stack.pop() != self.parentheses[char]:
                    return False
            else:
                stack.append(char)
        return not bool(stack)


solution = Solution()
print(solution.isValid("(({[[[]]]}()()()))"))
