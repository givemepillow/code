class Solution:
    romans = {
        1: "I", 4: "IV",
        5: "V", 9: "IX",
        10: "X", 40: "XL",
        50: "L", 90: "XC",
        100: "C", 400: "CD",
        500: "D", 900: "CM",
        1000: "M"
    }

    def intToRoman(self, num: int) -> str:
        if num:
            integer, quantity = self.int_and_quantity(num)
            return self.romans[integer] * quantity + self.intToRoman(num - (quantity * integer))
        return ''

    @staticmethod
    def int_and_quantity(num):
        for i in (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1):
            quantity = num // i
            if quantity > 0:
                return i, quantity


solution = Solution()
print(solution.intToRoman(int(input())))
