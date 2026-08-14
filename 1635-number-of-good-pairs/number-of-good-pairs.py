class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        freq = {}
        pairs = 0

        for num in nums:
            if num in freq:
                pairs += freq[num]
                freq[num] += 1
            else:
                freq[num] = 1

        return pairs