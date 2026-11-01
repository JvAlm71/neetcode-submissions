class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        if len(strs) == 0:
            return []

        subvet = defaultdict(list)


        for i in strs:
            chave = "".join(sorted(i))
            subvet[chave].append(i)

        return list(subvet.values())
