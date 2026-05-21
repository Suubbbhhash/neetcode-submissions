
from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res=[]
        for i in range (len(strs)):
            if strs[i]== None:
                continue
            sub=[]
            sub.append(strs[i])
            
            for j in range(i+1,len(strs)):
                if Counter(strs[i])==Counter(strs[j]) and strs[j] is not None:
                    sub.append(strs[j])
                    strs[j]=None
                    

            res.append(sub)
        return res

            


