class Solution:
    def isValid(self, s: str) -> bool:
        

        combs = {")": "(", "}": "{", "]": "["}

        result = []

        for parentese in s:

            if parentese in combs.values():
                result.append(parentese)

            else:

                if not result:
                    return False


                if result[-1] != combs[parentese]:
                    return False


                
                result.pop()
        

        return len(result) == 0



                