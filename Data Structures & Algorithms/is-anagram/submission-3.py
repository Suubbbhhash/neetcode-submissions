class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        res1=dict(Counter(s))
        res2=dict(Counter(t))
        if res1==res2:
            return True
        else:
            return False