class Solution:

    def encode(self, strs: list[str]) -> str:
        
        result = ""

        for palavra in strs:

            result += str(len(palavra)) + "#" + palavra

        

        return result
    
    
    
    def decode(self, s: str) -> list[str]:
        
        i = 0
        result =  []
        while i < len(s):
            
            j=i
            
            while s[j] != "#":
                j += 1
                
            
            tam_word = int(s[i:j])
            
            palavra = s[j+1: j + 1+tam_word]
            
            
            result.append(palavra)
            i = j + 1 + tam_word
            
        
        return result