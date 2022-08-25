class Solution:
    """ 
    Solution: has method to sort color
    """
    def sortColors(self, nums: List[int]) -> None:
        """
        sorts the color using buble sort
        attribute:
            nums: list of colors
            """
   
        for i in range(0, len(nums) - 1):
            for j in range(0, len(nums) - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                
