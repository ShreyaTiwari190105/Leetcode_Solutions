class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        freq={}

        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] +=1
        
        ans = 0

        for num in freq:
            if freq[num] == 1:
                ans += num
        return ans