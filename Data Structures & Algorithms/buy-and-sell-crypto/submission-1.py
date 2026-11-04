class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        minprice = float("inf")
        res = []
        for i, precos in enumerate(prices):

            if precos < minprice:
                minprice = precos
            else:
                prob = precos - minprice
                res.append(prob)


        if len(res) != 0:

            maior_val = max(res)

            if maior_val > 0:
            
                return maior_val

        return 0
