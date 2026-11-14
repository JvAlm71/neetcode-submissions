#Complexidade Máxima O(N+2M)
#O(N+2M)

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        for i, token in enumerate(tokens):
                if token == "+":
                    stack.append(stack.pop() + stack.pop())
                elif token == "-":
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(b - a)
                elif token == "*":
                    stack.append(int(stack.pop()*stack.pop()))
                elif token == "/":
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(int(b/a))
                else:
                    stack.append(int(token))
        

        return stack[0]