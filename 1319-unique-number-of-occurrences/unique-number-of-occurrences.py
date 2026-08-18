class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq={}

        for num in arr:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1
        
        occur = set(freq.values())
        if len(occur) == len(freq):
            return True
        
        return False