class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
            
        s= str(x)
        length = len(s)
        
        for i in range(length//2):
            if s[i] != s[length-i-1]:
                return False
            
        return True

