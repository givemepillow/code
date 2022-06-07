from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        value = 1
        nums.sort()
        for number in nums:
            if number > value:
                return value
            elif number == value:
                value += 1
        return value
