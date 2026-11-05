class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # abc ordenar -> abc, bac-> abc O(1)

        chaves = {}

        for string in strs:

            key = tuple(sorted(string))

            if not key in chaves:
                chaves[key]= []

            chaves[key].append(string)
        

        return list(chaves.values())