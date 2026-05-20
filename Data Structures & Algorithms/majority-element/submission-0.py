from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res=dict(Counter(nums))
        for key,value in res.items():
            if value >= len(nums)/2:
                return key