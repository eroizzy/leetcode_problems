class Solution:
    def isPalindrome(self, x: int) -> bool:
        return self.recursivePalindrome(str(x))
    
    def recursivePalindrome(self, temp: str) -> bool:
        if len(temp) < 2:
            return True
        if temp[0] == temp[-1]:
            return self.recursivePalindrome(temp[1:-1])
        else:
            return False


sol: Solution = Solution()
test = "12344321"
result = sol.isPalindrome(test)
print( result )