class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subs = ""
        max_subs_len = 0
        for i in range(len(s)):
            if s[i] not in subs:
                subs += s[i]
            else:
                subs = subs[subs.index(s[i])+1 : ] + s[i]
            max_subs_len = max(max_subs_len, len(subs))
        return max_subs_len
