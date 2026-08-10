class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        right = len(s) - 1
        while s[right] == " ":
            right -= 1
    
        count = 0

        while right >= 0 and s[right] != " ":
            count += 1
            right -= 1

        return count
            
