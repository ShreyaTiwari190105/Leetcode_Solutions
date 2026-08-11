from collections import Counter
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common = Counter(words[0])
        
        for word in words:
            current = Counter(word)

            for char in common:
                common[char] = min(common[char], current[char])

        ans = []

        for char,count in common.items():
            for _ in range(count):
                ans.append(char)

        return ans