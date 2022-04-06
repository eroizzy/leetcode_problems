class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if s == "": 
            return 0 
                   
        elif len(s) == 1:
            return 1  

        tempStr:str = ""
        largestUniqueSubstring = 0  

        for c in s:
            if c in tempStr:
                tempStr = tempStr[tempStr.index(c) + 1:]
            tempStr += c
            largestUniqueSubstring = max(len(tempStr),largestUniqueSubstring)
            
        return largestUniqueSubstring

sol = Solution()
s = "dvdf"
print ("\nLongest = "+str(sol.lengthOfLongestSubstring(s))+"\n")