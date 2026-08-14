class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        seen1 = set()
        seen2 = set()

        for num1 in nums1:
            if num1 not in seen1:
                seen1.add(num1)
        
        for num2 in nums2:
            if num2 not in seen2:
                seen2.add(num2)


        ans1 = list(seen1 - seen2)
        ans2 = list(seen2 - seen1)

        return(ans1 , ans2)