class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = {}

        for word in words:
            if word not in freq:
                freq[word] = 1
            else:
                freq[word] += 1

        sorted_words = sorted(freq , key = lambda word: (-freq[word], word))

        return sorted_words[:k]
