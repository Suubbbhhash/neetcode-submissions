class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        g=[0]*len(arr)
        for i in range(len(arr)):
            g[i]=(abs(arr[i]-x),arr[i])
        g.sort()
        res=[]
        for i in range(k):
            res.append(g[i][1])
        res.sort()
        return res