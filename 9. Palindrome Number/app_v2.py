class Solution:
    def isPalindrome(self, x: int) -> bool:
        revertedNumber: int = 0
        print(revertedNumber)
        print(x)
        while x > revertedNumber:
            revertedNumber = revertedNumber * 10 + x % 10
            x = int(x/10)
            print(revertedNumber)
            print(x)
        return revertedNumber == x or x == revertedNumber/10

sol: Solution = Solution()

test = 1234567
test2 = 1234321

result = sol.isPalindrome(test)
result2 = sol.isPalindrome(test2)

print( result )
print( result2 )
        