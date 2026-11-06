class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        sorted_list = sorted(nums1 + nums2)
        n = len(sorted_list)
        meio = n // 2

        if n % 2 == 0:
            return (sorted_list[meio - 1] + sorted_list[meio]) / 2
        else:
            return (sorted_list[meio])