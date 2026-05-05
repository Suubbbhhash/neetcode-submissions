class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n=len(arr)
        res=[0]*n
        i=0
        while i < n:
            if i ==n-1:
                res[i]=-1
            else:
                arr1=arr[i+1:]
                res[i]=max(arr1)
            
            i+=1
        return res