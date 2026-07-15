class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            k=1
            for j in range(len(nums)):
                if i!=j:
                    k*=nums[j]
            
            result.append(k)

        return result
