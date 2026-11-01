class Solution:
    def isPalindrome(self, s: str) -> bool:

        
        start = 0
        end = len(s) - 1 # para nao dar erro de fim de vetor

        while start < end:

            while start < end and not s[start].isalnum():
                start += 1

            while start  < end  and not s[end].isalnum():
                end -= 1


            if s[start].lower() != s[end].lower():
                return False

            start += 1
            end -= 1
        return True


s = Solution()
string = "Was it a car or a cat I saw?"
result = s.isPalindrome(string)
print(result)

