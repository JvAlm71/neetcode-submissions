from typing import List
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        if len(nums) == 0:
            return -1

        # voce cria o count
        count = {}

        for i in range(0, len(nums)):
            count[nums[i]] = 1 + count.get(nums[i],0)


        return heapq.nlargest(k, count.keys(), key = count.get)
