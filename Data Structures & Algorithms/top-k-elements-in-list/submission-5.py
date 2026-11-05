from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        
        result = []
        meu_dict = defaultdict()
        
        
        for numero in nums:
            
            if numero in meu_dict:
                meu_dict[numero] += 1
            else:
                meu_dict[numero] = 1
                
        meu_dict_list = list(sorted(meu_dict,key = meu_dict.get,reverse= True))
        # print(meu_dict)
        
        
        for i in range(k):
            result.append(meu_dict_list[i])
            

        return result
            
            