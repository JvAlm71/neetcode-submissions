class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        count1 = {}
        count2 = {}

        if len(s) != len(t):
            return False


        for letras1 in s:

            if letras1 in count1:
                count1[letras1] +=1
            else:
                count1[letras1] = 1

        


        for letras2 in t:

            if letras2 in count2:
                count2[letras2] +=1
            else:
                count2[letras2] = 1

        
        if count1 == count2:
            return True

        
        return False