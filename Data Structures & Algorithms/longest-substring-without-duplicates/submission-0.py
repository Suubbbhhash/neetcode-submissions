class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        tot=[]
        l=0
        res=0
        for r in range(len(s)):
            while s[r] in tot:
                tot.remove(s[l])
                l+=1
            tot.append(s[r])
            res=max(res,r-l+1)
        return res

        