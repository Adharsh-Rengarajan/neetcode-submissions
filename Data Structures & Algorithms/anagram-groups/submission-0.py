class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result=defaultdict(list)

        for i in strs:
            alphabetArray=[0]*26
            for j in i:
                alphabetArray[ord(j)-ord('a')]+=1

            result[tuple(alphabetArray)].append(i)

        return list(result.values())