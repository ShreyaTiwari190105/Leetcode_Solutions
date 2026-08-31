class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        freq = {}

        for num in nums:
            if num % 2 == 0:
                if num not in freq:
                    freq[num] = 1
                else:
                    freq[num] += 1
                

        for num in freq:
            if freq[num] == 1:
                return num
        
        return -1