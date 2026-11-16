class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        r=""
        x=0
        i=0
        for i in range (len(strs[0])):
            for j in range(1,len(strs)):
                if i>=len(strs[j]) or strs[0][x]!=strs[j][x]:
                    return r
            r+=strs[0][i]
            x+=1
        return r