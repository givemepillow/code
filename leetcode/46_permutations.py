from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def permutations(elements):
            if len(elements) <= 1:
                yield elements
                return
            for perm in permutations(elements[1:]):
                for i in range(len(elements)):
                    yield perm[:i] + elements[0:1] + perm[i:]

        return [p for p in permutations(nums)]
