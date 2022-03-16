from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        try:
            while len(set([s[i] for s in strs])) == 1:
                i += 1
        except KeyError:
            i -= 1
        finally:
            return strs[0][0:i]


print(Solution().longestCommonPrefix(['dog', 'dom', 'ds', 'a']))
