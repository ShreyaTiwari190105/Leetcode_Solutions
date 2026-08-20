class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        current_sum = 0
        count = 0

        prefix_map = {0:1}

        for num in nums:
            current_sum += num

            required = current_sum -k

            if required in prefix_map:
                count += prefix_map[required]

            prefix_map[current_sum] = prefix_map.get(current_sum, 0) + 1

        return count