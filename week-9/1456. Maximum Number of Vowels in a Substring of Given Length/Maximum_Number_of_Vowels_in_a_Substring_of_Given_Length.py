class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        subs = ""
        count = 0
        max_vow = 0
        vow = "aeiou"
        for i in range(len(s)):
            subs += s[i]
            if s[i] in vow:
                count += 1
            if i >= k:
                if subs[0] in vow:
                    count -= 1
                subs = subs[1: ]
                
            max_vow = max(max_vow, count)
        return max_vow
        
