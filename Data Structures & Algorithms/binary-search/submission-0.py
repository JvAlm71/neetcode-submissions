class Solution:
    def search(self, nums: List[int], target: int)-> int:
        
        start = 0
        end = len(nums) - 1
        # a busca binaria divide o vetor em dois ate encontrar o valor
        # por isso tem O(log(n))
        for num in nums:

            mid = int((start + end) / 2)

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1


        return -1
            
