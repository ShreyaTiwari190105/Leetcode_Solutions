class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        ans = 0
        result = []
        for i in range(len(nums)):
            ans += nums[i]
            result.append(ans)
        return result
