class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i=0
        j=len(heights)-1
        areas=[]
        while i<j:
            area=(j-i)*(min(heights[i],heights[j]))
            if heights[i]<heights[j]:
                i+=1
            else:
                j-=1
            areas.append(area)
        return max(areas)

        