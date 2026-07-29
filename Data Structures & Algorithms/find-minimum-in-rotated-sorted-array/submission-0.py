class Solution:
    def findMin(self, nums: List[int]) -> int:
        minimum_value = float('inf')

        for i in nums:
            minimum_value = min(i, minimum_value)
        
        return minimum_value