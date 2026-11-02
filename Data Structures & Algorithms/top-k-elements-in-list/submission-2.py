class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:

        meu_dict = {}


        for i, nums in enumerate(nums):

            if nums in meu_dict:
                meu_dict[nums] += 1
                # print(meu_dict)
            else:
                # print(meu_dict)
                meu_dict[nums] = 1


        dict_ordenado = sorted(meu_dict,key = meu_dict.get,reverse= True)
        print(dict_ordenado)


        valor = []

        for val in range(k):
            valor.append(dict_ordenado[val])


        return list(valor)


