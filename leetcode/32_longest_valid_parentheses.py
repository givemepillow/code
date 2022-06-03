class Solution:
    parentheses = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    def longestValidParentheses(self, s: str) -> int:
        _max = 0
        stack = list()
        stack.append(-1)
        for i in range(len(s)):
            if s[i] not in self.parentheses:
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    _max = max(_max, i - stack[-1])
        return _max
