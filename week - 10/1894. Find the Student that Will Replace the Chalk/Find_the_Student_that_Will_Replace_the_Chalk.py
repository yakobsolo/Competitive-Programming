class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        left = k%sum(chalk)
        if left == 0:
            return 0
        for n in range(len(chalk)):
            if left < chalk[n]:
                return n
            left -= chalk[n]
