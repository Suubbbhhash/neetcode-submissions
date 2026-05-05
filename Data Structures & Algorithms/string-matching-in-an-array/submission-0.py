class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        out=[]
        for ss in words:
            for s in words:
                if ss==s:
                    continue
                if ss in s :
                    out.append(ss)
                    break
        return out
        