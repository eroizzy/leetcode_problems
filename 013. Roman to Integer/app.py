class Solution:
    def romanToInt(self, s: str) -> int:
        roman_values: dict = { "I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000 }
        total: int = 0
        len_of_s: int = len(s)
        for x in range(len_of_s):
            cur: int = roman_values[s[x]]
            if x < len_of_s - 1:
                if cur < roman_values[s[x+1]]:
                    cur = 0 - cur
            total = total + cur
            x = x + 1
        return total


if __name__ == "__main__":
    # test
    sol: Solution = Solution()
    s: str = "MCMXCIV"
    result: int = sol.romanToInt(s)
    print (result)
