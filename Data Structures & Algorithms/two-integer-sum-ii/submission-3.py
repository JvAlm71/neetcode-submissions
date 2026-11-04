class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:

        sum = {}
        sorted_numbers = sorted(numbers)
        for i, numbs in enumerate(numbers):

            num2 = target - numbs
            # print(num2)
            if num2 in sum:
                return [sum[num2] + 1, i +1]

            sum[numbs] = i
            # print(sum[i])

        # print(sum)


        return []
