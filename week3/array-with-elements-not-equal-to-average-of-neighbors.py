class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        count = 0
        for i in range(len(nums)):
            for j in range(1, len(nums) - 1):
                if (nums[j - 1] + nums[j + 1]) / 2 == nums[j]:
                    temp = nums[j]
                    nums[j] = nums[j + 1]
                    nums[j + 1] = temp
                    count = count + 1
                else:
                    count = count - 1
            if count == 2:
                break
        return nums
