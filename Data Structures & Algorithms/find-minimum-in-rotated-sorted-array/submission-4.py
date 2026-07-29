class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        min_value = float('infinity')
        if nums[r] > nums[l]:
            return nums[0]
       
        while l <= r:
            middle =  (l + r) // 2
            if(nums[middle]>nums[r]):
                l = middle + 1
            else:
                r = middle - 1
            min_value =  min(min_value, nums[middle])

        return min_value 