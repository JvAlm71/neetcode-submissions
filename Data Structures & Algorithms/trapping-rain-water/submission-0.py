from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:

        res = 0
        l = 0
        r = len(height) - 1

        leftmax= height[l]
        rightmax = height[r]

        while l < r:
            if leftmax < rightmax:
                l += 1
                leftmax = max(leftmax, height[l])
                res += leftmax - height[l]
            else:
                r -= 1
                rightmax = max(rightmax, height[r])
                res += rightmax - height[r]

        return res


s= Solution()
height = [0,2,0,3,1,0,1,3,2,1]
result = s.trap(height)
print(result)
