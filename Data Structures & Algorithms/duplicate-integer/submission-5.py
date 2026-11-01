class Solution:

    #! inneficient solution
    # def hasDuplicate(self, nums: List[int]) -> bool:

    #     for i in range(0,len(nums)):
    #         for j in range(i+1,len(nums)):
    #             if nums[i] == nums[j]:
    #                 return True
        
    #     return False



    def hasDuplicate(self, nums: list[int]) -> bool:

        nums_set = set(nums)
        if len(nums_set) != len(nums):
            return True
        return False
