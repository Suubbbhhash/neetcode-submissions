from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n=len(s1)
        for i in range(len(s2)-n+1):
            if s2[i] in s1:
                if Counter(s2[i:i+n])==Counter(s1):
                    return True
                
        return False

                
