class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count, countodd, prefix = 0, 0, defaultdict(int)
        for i in range(len(nums)):
            prefix[countodd] += 1
            
            if nums[i] % 2 == 1:
                countodd += 1
            
            if countodd >= k:
                countpossiblesubarraystart = countodd - k
                count += prefix[countpossiblesubarraystart]
                
        return count
