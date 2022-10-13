class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        lef, res = 0, 0
        for rig in range(len(nums)):
            if nums[rig] == 0:
                k -= 1
            while k < 0:
                if nums[lef] == 0:
                    k += 1
                lef += 1
            res = max(res, rig - lef + 1)
        return res
