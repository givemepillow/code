class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        i, j = 0, 0
        while i < len(haystack):
            if haystack[i] == needle[j]:
                while j < len(needle) and i + j < len(haystack):
                    if haystack[i + j] != needle[j]:
                        break
                    j += 1
                if j == len(needle):
                    return i
                j = 0
            i += 1
        return -1


print(Solution().strStr("mississippi", "issip"))
