class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        i=0
        res=[]
        
        while i<len(nums)-2:
            j=i+1
            k=len(nums)-1
            sub=[]
            while j<k:
                if nums[i]+nums[j]+nums[k]==0:
                   sub=[nums[i],nums[j],nums[k]]
                   if sub not in res:
                    res.append(sub)
                   j+=1
                   k-=1
                elif nums[i]+nums[j]+nums[k]>0:
                    k-=1
                elif nums[i]+nums[j]+nums[k]<0:
                    j+=1
            i+=1
            
        return res

        
