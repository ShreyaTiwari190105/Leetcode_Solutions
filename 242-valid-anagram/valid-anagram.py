from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hashmap1= Counter(s)
        hashmap2= Counter(t)

        return hashmap1 == hashmap2
