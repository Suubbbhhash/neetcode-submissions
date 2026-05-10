from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        res=dict(Counter(nums))
        a=False
        for values in res.values():
            if values>1:
                a= True
                break
            else:
                a= False
        return a
        