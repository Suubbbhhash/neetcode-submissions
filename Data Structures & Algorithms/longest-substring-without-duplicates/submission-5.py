class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res=[]
        c=[]
        for i in range(len(s)):
            if s[i] not in c:
                c.append(s[i])
            else:
                res.append(len(c))
                c=c[c.index(s[i])+1:]
                c.append(s[i])
            res.append(len(c))
        return max(res) if res else 0
