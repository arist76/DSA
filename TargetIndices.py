class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        # Sorting with bubble sort
        for each in range(len(nums)):
            for every in range(len(nums)-1):
                if nums[every] > nums[every + 1]:
                    nums[every], nums[every + 1] = nums[every + 1], nums[every]

        target_index = []
        for v, each in enumerate(nums):
            if each == target:
                target_index.append(v)

        return target_index
