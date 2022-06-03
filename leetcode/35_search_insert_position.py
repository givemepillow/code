from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)
        i = 0
        while left < right:
            i = (right + left) // 2
            element = nums[i]
            if element == target:
                return i
            elif element > target:
                right = i
            else:
                left = i + 1
        return i if nums[i] > target else i + 1


solution = Solution()
print(solution.searchInsert([1, 3, 5, 6], 0))
