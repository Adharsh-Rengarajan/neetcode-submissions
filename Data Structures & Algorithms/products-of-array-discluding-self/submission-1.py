class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        
        prefixMultiple = []
        suffixMultiple = []

        prefixval = 1
        suffixval = 1

        for i in range(len(nums)):
            prefixval *= nums[i]
            suffixval *= nums[len(nums)-i-1]

            prefixMultiple.append(prefixval)

            suffixMultiple.append(suffixval)



        for i in range(len(nums)):
            if i==0:
                result.append(suffixMultiple[len(nums)-i-2])
            elif i==len(nums)-1:
                result.append(prefixMultiple[i-1])
            else:
                result.append(prefixMultiple[i-1] * suffixMultiple[len(nums)-i-2])

    
        return result
