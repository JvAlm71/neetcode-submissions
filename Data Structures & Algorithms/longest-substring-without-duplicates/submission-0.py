class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        substring = set()
        l = 0
        result = 0

        for i in range(len(s)):
            while s[i] in substring:
                substring.remove(s[l])
                l += 1

            substring.add(s[i])
            result = max(result, i - l + 1)#pega na posição r, retira 
                                            # o elemento repetido e acrescenta
                                            #o proximo da substring
        return result

