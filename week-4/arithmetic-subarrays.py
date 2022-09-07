class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        out = []
        for i in range(len(l)):
            ls = []

            for j in range(l[i],r[i]+1):
                ls.append(nums[j])

            ls.sort()

            res = []
            for v in range(len(ls)-1):
                val = ls[v]-ls[v+1]
                res.append(val)

            if len(set(res)) == 1:
                out.append(True)
            else:
                out.append(False)
                
        return out
