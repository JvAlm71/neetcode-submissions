class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        s_list = list(s)
        count1 = {}
        t_list = list(t)
        count2 = {}

        if len(s_list) != len(t_list):
            return False


        for i in range(len(s_list)):

            if s_list[i] in count1:
                count1[s_list[i]] += 1
            else:
                count1[s_list[i]] = 1


        for i in range(len(t_list)):

            if t_list[i] in count2:
                count2[t_list[i]] += 1
            else:
                count2[t_list[i]] = 1


        if count1 == count2:
            return True

        return False
        # return count1, count2
        # return s_list,t_list
