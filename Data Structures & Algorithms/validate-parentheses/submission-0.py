#Criar uma forma de pilha para empilhar os brackets
# e depois coloca-lo, fazer uma verificação. se [, empilha, e somente
# será verdadeiro na hora que desempilhar ]
class Solution:
    def isValid(self, s: str) -> bool:

        pilha = []
        # o que voce empilha, com seu correspondente...
        pares = {"]" : "[", ")": "(", "}" : "{"}

        for char in s:
            # o elemento do vetor tiver armazenado nos pares, faça. Abertura
            if char in pares.values():
                pilha.append(char)
            
            elif char in pares:

                if not pilha or pilha[-1] != pares[char]:
                    return False
                pilha.pop()

            else:
                return False


        return not pilha

