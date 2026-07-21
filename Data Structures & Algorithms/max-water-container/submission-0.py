class Solution:
    def maxArea(self, heights: List[int]) -> int:

        maxArea=0

        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                minValue=min(heights[i], heights[j])
                maxArea=max(maxArea, minValue*(j-i))
        return maxArea