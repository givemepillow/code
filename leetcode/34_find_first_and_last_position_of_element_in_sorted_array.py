from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        index = self.binary_search(nums, target)
        left = index
        right = index
        if index != -1:
            if index < len(nums):
                while right + 1 < len(nums) and nums[right + 1] == target:
                    right += 1
            if index > 0:
                while left - 1 > -1 and nums[left - 1] == target:
                    left -= 1
        return [left, right]

    def binary_search(self, nums: List[int], target: int):
        left = 0
        right = len(nums)
        while left < right:
            i = (right + left) // 2
            element = nums[i]
            if element == target:
                return i
            elif element > target:
                right = i
            else:
                left = i + 1
        return -1


solution = Solution()
print(solution.searchRange([2, 3, 3, 3], 2))
