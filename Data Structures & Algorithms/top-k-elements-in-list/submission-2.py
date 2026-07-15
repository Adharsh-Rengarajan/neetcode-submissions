class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        array={}
        result=set()

        for i in nums:
            if i not in array:
                array[i]=1
            else:
                array[i]+=1
        # print(array)
        values=list(array.values())
        values.sort(reverse=True)
        values=values[:k]
        # print(values)
        for i in values:
            for j in array:
                if(array[j]==i):
                    result.add(j)
        return list(result)