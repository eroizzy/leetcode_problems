class Solution:
    def isPalindrome(self, x: int) -> bool:
        revertedNumber: int = 0
        while x > revertedNumber:
            revertedNumber = revertedNumber * 10 + x % 10
            x = int(x/10)
        return revertedNumber == x or x == int(revertedNumber/10)

sol: Solution = Solution()

test = 1234567
test2 = 1000

result2 = sol.isPalindrome(test2)


print( result2 )
        