class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        poin = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[poin], nums[i] = nums[i], nums[poin]
                poin = poin + 1
                
