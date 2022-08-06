class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if s == "": 
            return 0 
                   
        elif len(s) == 1:
            return 1  

        tempStr:str = ""
        largestUniqueSubstring = 0
        sLength = len(s)
        for x in range(sLength):
            tempStr = s[x]
            for y in range(sLength-x-1):
                secondPointer = y + x + 1
                if s[secondPointer] not in tempStr:
                    tempStr += s[secondPointer]
                else:
                    break;
            if len(tempStr) > largestUniqueSubstring:
                        largestUniqueSubstring = len(tempStr)
        return largestUniqueSubstring

sol = Solution()
s = "abcabcbb"
print (sol.lengthOfLongestSubstring(s))