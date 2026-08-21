class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        words = s.split()

        if len(pattern) != len(words):
            return False

        m1={}
        m2={}

        for i in range(len(pattern)):
            char = pattern[i]
            word = words[i]

            if char in m1:
                if m1[char] != word :
                    return False

            if word in m2:
                if m2[word] != char:
                    return False

            m1[char] = word 
            m2[word] = char
        
        return True