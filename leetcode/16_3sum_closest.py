from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        best_sum = sum(nums[0:3])
        min_diff = abs(sum(nums[0:3]) - target)
        for i in range(len(nums)):
            a = nums[i]
            start = i + 1
            end = len(nums) - 1
            while start < end:
                b = nums[start]
                c = nums[end]
                current_sum = sum((a, b, c))
                current_diff = abs(target - current_sum)
                if current_diff == 0:
                    return target
                elif current_diff < min_diff:
                    min_diff = current_diff
                    best_sum = current_sum
                if current_sum < target:
                    start += 1
                else:
                    end -= 1
        return best_sum


solution = Solution()
print(solution.threeSumClosest([0, 0, 0], 1) == 0)

print(solution.threeSumClosest([-1, 2, 1, -4, -90, 100, -9], 1) == 1)
print(solution.threeSumClosest([1, 1, 1, 0], -100) == 2)
print(solution.threeSumClosest([-3, -2, -5, 3, -4], -1) == -2)
print(solution.threeSumClosest([0, 2, 1, -3], 1) == 0, solution.threeSumClosest([0, 2, 1, -3], 1))
print(solution.threeSumClosest([1, 2, 4, 8, 16, 32, 64, 128], 82) == 82,
      solution.threeSumClosest([1, 2, 4, 8, 16, 32, 64, 128], 82))

