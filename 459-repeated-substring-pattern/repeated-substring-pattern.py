class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for length in range(1, len(s)):
            if len(s) % length == 0:
                pattern = s[:length]
                match = True

                for i in range(len(s)):
                    if s[i] != pattern[i % length]:
                        match = False
                        break

                if match:
                    return True
        return False