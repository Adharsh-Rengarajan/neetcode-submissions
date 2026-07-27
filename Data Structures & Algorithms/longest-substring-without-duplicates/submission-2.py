class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        uniqueElements = set()
        l = 0
        maxValue = 0

        for i in range(len(s)):
            while s[i] in uniqueElements:
                uniqueElements.remove(s[l])
                l += 1
            uniqueElements.add(s[i])
            maxValue = max(maxValue, i - l + 1)

        return maxValue