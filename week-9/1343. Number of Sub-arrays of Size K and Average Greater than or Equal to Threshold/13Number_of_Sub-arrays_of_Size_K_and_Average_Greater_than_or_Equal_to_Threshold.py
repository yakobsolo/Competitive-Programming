class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0
        avg = 0
        sums = 0
        for i in range(len(arr)):
            if i >= k:
                sums -= arr[i - k]
            sums += arr[i]
            avg = sums / k
            
            if avg >= threshold and i >= k - 1:
                count += 1
        return count
