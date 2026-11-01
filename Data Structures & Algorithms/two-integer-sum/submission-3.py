class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        
        dict_nums ={}
        
        
        for i, num in enumerate(nums,0):
            
            num2 = target - num
            
            if num2 in dict_nums:
                return [dict_nums[num2], i]
            
            dict_nums[num] = i
        
        return []
        
        