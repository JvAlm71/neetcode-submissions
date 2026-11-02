class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:

        contain = set()

        for i in nums:

            if i in contain:
                return True
            
            contain.add(i)

        return False