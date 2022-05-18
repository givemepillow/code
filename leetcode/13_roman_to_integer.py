class Solution:
    romans = {
        "I": 1, "IV": 4,
        "V": 5, "IX": 9,
        "X": 10, "XL": 40,
        "L": 50, "XC": 90,
        "C": 100, "CD": 400,
        "D": 500, "CM": 900,
        "M": 1000
    }

    def romanToInt(self, s: str) -> int:
        integer = 0
        if s:
            i = 0
            for roman in dict(sorted(self.romans.items(), key=lambda item: item[1], reverse=True)):
                if s[i:i + 3] == 3 * roman:
                    integer += self.romans[roman] * 3
                    i += 3
                elif s[i:i + 2] == 2 * roman:
                    integer += self.romans[roman] * 2
                    i += 2
                elif s[i:i + 2] == roman:
                    integer += self.romans[roman]
                    i += 2
                elif s[i:i + 1] == roman:
                    integer += self.romans[roman]
                    i += 1

        return integer


solution = Solution()
print(solution.romanToInt(input()))
