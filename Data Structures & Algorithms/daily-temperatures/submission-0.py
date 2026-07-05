class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[0]*len(temperatures)
        for i in range(len(temperatures)):
            for x in range(i,len(temperatures)):
                if temperatures[i]<temperatures[x]:
                    res[i]=abs(i-x)
                    break
                else:
                    None
        return res