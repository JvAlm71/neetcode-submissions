class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        sums = {}

        for i, numero in enumerate(nums):
            num2 = target - numero

            if num2 in sums:
                return [sums[num2], i]
            
            sums[numero] = i
            

        return []