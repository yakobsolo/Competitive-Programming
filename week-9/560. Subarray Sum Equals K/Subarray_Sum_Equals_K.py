class Solution:
    " T.C - O(n)
      S.C - O(1)"
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        cursum = 0
        diff = 0
        prefixsum = {0: 1}
        for n in nums:
            cursum += n
            diff = cursum - k
            res += prefixsum.get(diff, 0)
            prefixsum[cursum] = 1 + prefixsum.get(cursum, 0)
        return res
    
    
    
 # tried to do with sliding windows technique       
#         l = 0
#         sums = 0
#         count = 0
        
#         for i in range(len(nums)):
            
#             sums += nums[i]
#             if sums >= k:
#                 if sums > k:
#                     sums -= nums[l]
#                     l += 1
#                     if nums[i] == k:
#                         count += 1
#                         break
#                     elif sums > k:
#                         sums -= nums[l]
#                         l += 1
#                         break
#                     else:
#                         break
                
#                 count += 1
                
#                 sums -= nums[l]
#                 l += 1
               
#         return count
        
