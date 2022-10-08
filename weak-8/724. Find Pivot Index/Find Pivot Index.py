class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        s=sum(nums)
        i=0
        l=len(nums)
        temp=0
        while i<l:
            s-=nums[i]
            if temp==s:
                return i
            temp+=nums[i]
            i+=1
        return -1
# i tried with two pointer seams like i have made some mistake
#         right_sum = 0
#         for i in range(1, len(nums)):
#             right_sum = right_sum + nums[i]
#         if right_sum == 0:
#             return 0
#         left_sum = 0
#         for i in range(len(nums) -2 , 0):
#             left_sum = left_sum + nums[i]
#         if left_sum == 0:
#             return 0
#         tot_sum = 0
#         for i in range(len(nums)):
#             tot_sum = tot_sum + nums[i]
        
            
#         lef_sum = 0
#         rig_sum = 0
#         le = 0
#         ri = len(nums) - 1
        
#         while lef_sum != rig_sum:
#             if lef_sum < tot_sum//2:
#                 lef_sum = lef_sum + nums[le]
#             if rig_sum < tot_sum//2:
#                 rig_sum = rig_sum + nums[ri]
#             le += 1
#             ri -= 1
#         if lef_sum == rig_sum:
#             le += 1
#             return le
#         return -1
          
