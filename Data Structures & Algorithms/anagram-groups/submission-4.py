class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        anagram = {}


        for i, palavra in enumerate(strs):

            # ABC -> ABC; BAC -> ABC
            chave = tuple(sorted(palavra))
            
            if chave not in anagram:
                anagram[chave] = []

            anagram[chave].append(palavra)


        return list(anagram.values())