# import math
# class Solution:
#     def minEatingSpeed(self, piles: list[int], h: int) -> int:
        
#         speed = 1
        
#         while piles:
#             total_time = 0
            
#             for pile in piles:
#                 total_time += math.ceil(pile/speed)
            
#             if total_time <= h:
#                 return speed

#             speed += 1
        
#         return speed





class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l + r) // 2

            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p) / k)
            if totalTime <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        return res