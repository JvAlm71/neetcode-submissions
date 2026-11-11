class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        
        max_profit = float("inf")
        result = []
        max_val = 0
        
        for precos in prices:
            
            if precos < max_profit:
                max_profit = precos
            else:
                prob = precos - max_profit
                result.append(prob)
        
        if len(result) != 0:
            max_val = max(result)
            
        if max_val > 0:
            return max_val

        return 0
