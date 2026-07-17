class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        result = [1]*n
        k=1

        for i in range(len(nums)):
            k*=nums[i]
            result[i]=k
        # print(result)
        k=1

        for i in range(len(nums)-1,-1,-1):
            if(i==len(nums)-1):
                result[i] = result[i-1]
            elif(i==0):
                result[i]=k
            else:
                result[i]=k*result[i-1]
            
            k = k*nums[i]
            


        return result