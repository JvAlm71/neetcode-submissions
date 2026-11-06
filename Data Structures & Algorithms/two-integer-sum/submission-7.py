from collections import defaultdict
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        
        
        soma = defaultdict()
        
        
        for i, numero in enumerate(nums):
            
            complemento = target - numero
            
            if complemento in soma:
                return [soma[complemento], i]
            
            soma[numero] = i
            
        
        return []