from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        result = []
        if not words:
            return result
        one_word_len = len(words[0])
        words_number = len(words)
        _set = set(words)
        words = sorted(words)
        i = 0
        while i < len(s):
            if s[i:i + one_word_len] in words:
                _words = []
                flag = True
                for j in range(0, words_number * one_word_len, one_word_len):
                    w = s[i + j:i + j + one_word_len]
                    if w in _set:
                        _words.append(w)
                    else:
                        flag = False
                        break
                if flag and sorted(_words) == words:
                    result.append(i)
            i += 1
        return result


solution = Solution()

print(solution.findSubstring("barfoofoobarthefoobarman", ["bar", "foo", "the"]))
print(solution.findSubstring("wordgoodgoodgoodbestword", ["word", "good", "best", "good"]))
print(solution.findSubstring("aaaaaaaaaaaaaa", ["aa", "aa"]))
# assert solution.findSubstring("barfoofoobarthefoobarman", ["bar", "foo", "the"]) == [9, 6, 12]
# assert solution.findSubstring("wordgoodgoodgoodbestword", ["word", "good", "best", "good"]) == [8]
