class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0

        count = {}
        l = 0
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0)+1
            while count[s[r]] > 1:
                count[s[l]] -= 1
                l += 1
            length = max(length, 1+r-l)
        return length
