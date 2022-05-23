from typing import List


# O(n^(k-1)) => O(n^3)
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = set()
        nums = sorted(nums)
        for start1 in range(len(nums) - 3):
            for start2 in range(start1 + 1, len(nums) - 2):
                start = start2 + 1
                end = len(nums) - 1
                while start < end:
                    numbers = (nums[start1], nums[start2], nums[start], nums[end])
                    _sum = sum(numbers)
                    # print(_tuple)
                    if _sum == target:
                        result.add(numbers)
                        end -= 1
                        start += 1
                    elif _sum > target:
                        end -= 1
                    else:
                        start += 1
        return result


solution = Solution()
print(solution.fourSum([-3, -1, 0, 2, 4, 5], 2))
print(len(solution.fourSum([-3, -2, -1, 0, 0, 1, 2, 3], 0)) == 8)
