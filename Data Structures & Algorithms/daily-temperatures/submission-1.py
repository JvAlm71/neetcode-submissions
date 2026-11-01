from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n

        for i in range(n):
            countdays = 0  # reinicia a cada nova posição
            for j in range(i + 1, n):
                countdays += 1
                if temperatures[j] > temperatures[i]:
                    result[i] = countdays
                    break
        return result
