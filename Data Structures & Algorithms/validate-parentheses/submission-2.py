class Solution:
    def isValid(self, s: str):

        combs = {")":"(", "}":"{","]":"["}

        stack = []

        for c in s:
            if c in combs.values():
                stack.append(c)


            else:
                if not stack:
                    return  False

                if stack[-1] != combs[c]:
                    return False

                stack.pop()


            

        return len(stack) == 0