from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        if len(nums) < 2:
            return
        i = len(nums) - 1
        _i, _j = len(nums) - 1, 0
        value = max(nums) + 1
        while i != 0:
            j = i - 1
            while j >= 0:
                if nums[i] > nums[j]:
                    if i <= _i and j >= _j:
                        if _j == j and nums[i] > value:
                            pass
                        else:
                            _i = i
                            _j = j
                            value = nums[i]
                j -= 1
            i -= 1
        nums[_i] += nums[_j]
        nums[_j] = nums[_i] - nums[_j]
        nums[_i] -= nums[_j]
        self.sort(nums, _j + 1, len(nums))

    @staticmethod
    def sort(array, start, end):
        for i in range(start, end):
            j = i
            while j > start and array[j - 1] > array[j]:
                temp = array[j]
                array[j] = array[j - 1]
                array[j - 1] = temp
                j -= 1


solution = Solution()
_list = [3, 5, 2]
solution.nextPermutation(_list)
print(_list)

_list = [1, 3, 2]
solution.nextPermutation(_list)
print(_list)

_list = [4, 2, 0, 2, 3, 2, 0]  # [4,2,0,3,0,2,2]
solution.nextPermutation(_list)
print(_list)
