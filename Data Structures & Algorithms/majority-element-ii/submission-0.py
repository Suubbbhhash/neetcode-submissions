from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        s=int(len(nums)/3)
        res=[]
        freq=dict(Counter(nums))
        for key,value in freq.items():
            if value > s:
                res.append(key)
        return res
