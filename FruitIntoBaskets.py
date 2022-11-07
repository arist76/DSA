class Solution:
    def totalFruit(self, fr: list[int]) -> int:
        l = i = 0
        m = 0
        bs = [-1,-1]
        for r in range(len(fr)):
            if fr[r] != bs[1]:
                if fr[r] != bs[0]: l = i
                i = r
                bs[0], bs[1] = bs[1], fr[r]
            m = max(m, r - l + 1)            

        return m
