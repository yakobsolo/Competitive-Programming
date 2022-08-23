class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        leng = len(nums)
      
        count_list = []
        for i in range(leng):
            count = 0
            j = i + 1
            for j in range(leng):
                if j != i and nums[j] < nums[i]:
                    count = count + 1
                
            count_list.append(count)
        return count_list
    
obj1 = Solution()
nums = [8,1,2,2,3]
obj1.smallerNumbersThanCurrent(nums)
