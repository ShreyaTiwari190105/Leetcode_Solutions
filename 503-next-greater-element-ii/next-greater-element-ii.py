class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        n = len(nums)
        answer = [-1] * n

        for i in range(2*n):
            index = i % n
            
            while stack and nums[index] > nums[stack[-1]]:
                previous = stack.pop()
                answer[previous] = nums[index]

            if i < n:
                stack.append(index)

        return answer