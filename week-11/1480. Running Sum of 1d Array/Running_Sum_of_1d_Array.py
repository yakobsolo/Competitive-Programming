class Solution:
  """
  T.C = O(n)
  S.C = O(1)
  """
    def runningSum(self, nums: List[int]) -> List[int]:
        
      
        for i in range(1, len(nums)):
            nums[i] = nums[i] + nums[i -1]
        return nums
