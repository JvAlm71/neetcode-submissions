class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0
        elements = set()
        left = 0

        for right in range(len(s)):

            while s[right] in elements:
                elements.remove(s[left])
                left += 1

            elements.add(s[right])

            count = max(count, right - left + 1)

        return count