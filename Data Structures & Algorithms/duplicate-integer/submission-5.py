class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        res=[]
        b=False
        for i in nums:
            if i in res:
                b=True
            else:
                res.append(i)
                
        return b