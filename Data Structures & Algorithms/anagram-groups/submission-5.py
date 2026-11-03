class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:


        anagramas = {}

        for i , palavras in enumerate(strs):

            chave = tuple(sorted(palavras))

            if chave not in anagramas:
                anagramas[chave] = []
            
            anagramas[chave].append(palavras)


        
        return list(anagramas.values())
        
