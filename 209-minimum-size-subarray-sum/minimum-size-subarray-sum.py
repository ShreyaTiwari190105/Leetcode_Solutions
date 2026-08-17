class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        current_sum = 0
        min_length = float('inf')

        for right in range(len(nums)):
            current_sum += nums[right]

            while current_sum >= target:
                window_length = right - left + 1

                if min_length > window_length:
                    min_length = window_length

                current_sum -= nums[left]
                left += 1

        if min_length == float('inf'):
            return 0

        return min_length

                 
            
