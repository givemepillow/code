class Solution:
    def convert(self, s: str, numRows: int) -> str:
        matrix_size = 0
        zig_size = (numRows - 2) if (numRows - 2) > 0 else 0
        s_len = len(s)
        while True:
            if s_len > 0:
                s_len -= numRows
                matrix_size += 1
            else:
                break
            if s_len > 0:
                s_len -= zig_size
                matrix_size += zig_size
            else:
                break
        matrix = {}
        for i in range(numRows):
            matrix[i] = {j: ' ' for j in range(matrix_size)}
        i = 0
        coords = self.coordinates(numRows, zig_size)
        while i < len(s):
            r, c = next(coords)
            matrix[r][c] = s[i]
            i += 1
        result = ''
        for row in matrix.values():
            result += ' '.join(row.values()) + '\n'
        # result = ''.join([v for row in matrix.values() for v in row.values() if v != ' '])
        return result

    @staticmethod
    def coordinates(rows_number, zig_line):
        c = 0
        r = 0
        while True:
            for i in range(rows_number):
                r = i
                yield r, c
            for _ in range(zig_line):
                r -= 1
                c += 1
                yield r, c
            c += 1


print(Solution().convert("PAYPALISHIRING", 3))
