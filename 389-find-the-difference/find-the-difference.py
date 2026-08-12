class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        freq = {}

        for char in s:
            if char not in freq:
                freq[char] = 1
            else:
                freq[char] +=1
        
        for char in t:
            if char not in freq:
                return char
            
            if freq[char] == 0:
                return char
            
            freq[char] -= 1

        return ""

            