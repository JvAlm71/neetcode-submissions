class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        count1 = {}
        count2 = {}

        if len(s) != len(t):
            return False


        for i, char1 in enumerate(s):
            if char1 in count1:
                count1[char1] +=1
                # print(count1)
            else:
                count1[char1] =1



        for i, char2 in enumerate(t):
            if char2 in count2:
                count2[char2] +=1
                # print(count2)
            else:
                count2[char2] =1


        if count1 == count2:
            return True


        return False
