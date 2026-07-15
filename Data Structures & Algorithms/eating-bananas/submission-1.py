class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res=r

        while l<=r:
            mid=(l+r)//2
            th=0

            for x in piles:
                th+=math.ceil(float(x)/mid) 

            if(th<=h):
                res=mid
                r=mid-1
            else:
                l=mid+1

        return res