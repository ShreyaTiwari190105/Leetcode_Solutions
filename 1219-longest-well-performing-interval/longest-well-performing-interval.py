class Solution:
    def longestWPI(self, hours: list[int]) -> int:
        freq = {}
        prefix_sum = 0
        count = 0

        for i, num in enumerate(hours):
            if num > 8 :
                prefix_sum += 1
            else:
                prefix_sum -= 1

            if prefix_sum > 0:
                count = i + 1

            else:
                if prefix_sum - 1 in freq:
                    count = max(count, i - freq[prefix_sum - 1])

            if prefix_sum not in freq:
                freq[prefix_sum] = i

        return count

         