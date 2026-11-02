class Solution:
    def groupAnagrams(self, strs: list[str]) -> List[List[str]]:

        anagrams = {}


        for palavras in range(len(strs)):

            chaves = tuple(sorted(strs[palavras]))
            if chaves not in anagrams:
                anagrams[chaves] = []
            anagrams[chaves].append(strs[palavras])


        return list(anagrams.values())