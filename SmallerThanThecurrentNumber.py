class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        l = []
        for each in nums:
            count = 0
            for every in nums:
                if each > every:
                    count += 1
            l.append(count)

        return l
