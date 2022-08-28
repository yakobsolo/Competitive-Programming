class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        for i in range(len(intervals)):
            mer_res = []
            intervals.sort()
            for interval in intervals:
                if mer_res == [] or mer_res[-1][1] < interval[0]:
                    mer_res.append(interval)
                else:
                    mer_res[-1][1] = max(mer_res[-1][1], interval[1])
                
            return mer_res
