import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        answ = 0
        while left <= right:
            mid = (left + right)//2 #скорость

            t = 0
            for p in piles:
                t += math.ceil(p/mid)
            
            if t<=h:
                answ = mid
                right = mid - 1
            else:
                left = mid + 1
        return answ

