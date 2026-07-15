class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for i in nums:
            count[i] = 1 + count.get(i,0)
        
        frequency = [[] for _ in range(len(nums)+1)]

        for i, j in count.items():
            frequency[j].append(i)

        result=[]

        for i in range(len(nums),-1,-1):
            for j in frequency[i]:
                result.append(j)
                if(len(result)==k):
                    return result

        return result