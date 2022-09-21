class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        count = {}
        for x in range(len(arr)) :
            if arr[x] not in count : count[arr[x]] = 0
            count[arr[x]] += 1
        
        counter = 0
        add = 0
        for temp in sorted(count.values(), reverse = True) :
            add += temp
            counter += 1
            if add >= len(arr)//2 : break
        return counter
