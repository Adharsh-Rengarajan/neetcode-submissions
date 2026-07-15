class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result=defaultdict(list)

        for i in strs:
            hashMap=[0]*26
            for j in i:
                hashMap[ord(j)-ord('a')]+=1
            
            result[tuple(hashMap)].append(i)
        
        return list(result.values())