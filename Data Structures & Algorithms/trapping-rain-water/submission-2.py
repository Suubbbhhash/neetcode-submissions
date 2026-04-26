class Solution:
    def trap(self, height: List[int]) -> int:
        i=0
        j=len(height)-1
        maxL=[]
        maxR=[]
        mL,mR=0,0
        while i<len(height) and j>=0:
            mL=max(mL,height[i])
            maxL.append(mL)
            mR=max(mR,height[j])
            maxR.append(mR)
            
            i+=1
            j-=1
        maxR.reverse()
        x=0
        summ=0
        res=0
        while x<len(height):
            summ=min(maxL[x],maxR[x])-height[x]
            res=res+summ
            x+=1
        return res

        