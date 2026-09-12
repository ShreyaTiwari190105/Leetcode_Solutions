class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefix = 0
        ans = 0

        freq = {0: -1}

        for i in range(len(nums)):

            if nums[i] == 0:
                prefix -= 1

            else:
                prefix += 1

            if prefix in freq:
                ans = max(ans, i - freq[prefix])
            else:
                freq[prefix] = i

        return ans