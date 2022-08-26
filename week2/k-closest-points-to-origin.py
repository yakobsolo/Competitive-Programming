class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = {}
        dis_list = []
        min_points = []
    
        for i in points:
            dis = ((((i[0] - 0) ** 2) )+ (((i[1] - 0) ** 2))) ** 0.5
        
            if dis in dis_list:
                dis = dis + 0.1
                if dis in dis_list:
                    dis = dis + 0.1
            res.update({dis: i})
            dis_list.append(dis)
        dis_list.sort()
        for j in range(0, k):
            min_points.append(res.get(dis_list[j]))
        return min_points
