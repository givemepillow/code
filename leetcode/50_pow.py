class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 1:
            return 1
        elif x == -1:
            return -1 if n % 2 else 1
        result = 1
        for _ in range(abs(n)):
            result = result * x
            if result > 100000 or 0 <= result < 0.000001:
                break
        return 1 / result if n < 0 else result


print(Solution().myPow(-2,2))
