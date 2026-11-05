class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        
        numeros = set(nums)
        
        consecutives = 0
        atual = 0
        tamanho = 0
        for n in numeros:
            
            if n - 1 not in numeros:
                atual = n
                tamanho = 1
                
            while (atual + 1) in numeros:
                atual += 1
                tamanho +=1
            
            if tamanho > consecutives:
                consecutives = tamanho
                
                
        return consecutives
