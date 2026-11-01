from typing import List

class Solution:
    def maxArea(self, heights: List[int]) -> int:

        res = 0
        for i in range(0, len(heights)):
            for j in range( i + 1, len(heights)):
                height_min = min(heights[i], heights[j])
                dist = (j+1) - (i+1)
                res = max(res,height_min*dist)

        return res



