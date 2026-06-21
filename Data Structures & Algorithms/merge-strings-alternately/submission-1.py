class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n=len(word1)
        m=len(word2)
        if n < m:
            w1=word1
            w2=word2[:n]
            w3=word2[n:]
        elif n > m:
            w2=word2
            w1=word1[:m]
            w3=word1[m:]
        else:
            w1=word1
            w2=word2
            w3=""
        res=""
        for l in range (len(w1)):
            res += w1[l]
            res += w2[l]
        res += w3
        return res
        

        