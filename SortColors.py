class Solution:
    def sortColors(self, nums: List[int]) -> None:
        for each in range(len(nums)):
            for every in range(len(nums)-1):
                if nums[every] > nums[every + 1]:
                    nums[every], nums[every + 1] = nums[every + 1], nums[every]
                    
