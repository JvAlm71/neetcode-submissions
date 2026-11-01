from typing import List

class Solution:
    def findMinBruteForce(self, nums: List[int]) -> int:

        return min(nums)

    def findMin(self, nums: List[int]) -> int:

        left = 0
        right = len(nums) - 1

        while left < right:

            m = (left+ right)//2

            if nums[m] < nums[right]:
                right = m
            else:
                left = m + 1

        return nums[left]