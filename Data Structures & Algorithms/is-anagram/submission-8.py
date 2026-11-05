class Solution:
    def isAnagram(self, s: str, t: str) -> bool:


        if len(s) != len(t):
            return False
        
        count1 ={}
        count2 = {}

        for l1 in s:
            if l1 in count1:
                count1[l1] +=1
            else:
                count1[l1] = 1
        
        for l2 in t:
            if l2 in count2:
                count2[l2] +=1
            else:
                count2[l2] = 1
        
        if count1 == count2:
            return True
        
        return False