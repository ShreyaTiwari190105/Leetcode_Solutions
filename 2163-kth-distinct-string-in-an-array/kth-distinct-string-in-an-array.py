class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        freq={}

        for s in arr:
            if s not in freq:
                freq[s] = 1
            else:
                freq[s] += 1

        count = 0
        for s in arr:
            if freq[s] == 1:
                count +=1
        
                if count == k :
                    return s
        
        return ""
