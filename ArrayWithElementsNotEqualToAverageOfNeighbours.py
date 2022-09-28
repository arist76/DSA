class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        ans = []
        sorted_nums = sorted(nums)
        for index in range(len(sorted_nums)//2):
            ans.append(sorted_nums[index])
            ans.append(sorted_nums[-(index+1)])
        if len(nums) % 2 != 0:
            ans.append(sorted_nums[len(sorted_nums)//2])
        return ans
