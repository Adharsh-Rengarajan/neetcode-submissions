class Solution:
    def maxArea(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        maxArea = min(nums[l], nums[r]) * (r-l)

        while(l<r):
            area = min(nums[l], nums[r]) * (r-l)
            maxArea = max(area, maxArea)
            if(nums[l]<=nums[r]):
                l+=1
            else:
                r-=1

        return maxArea