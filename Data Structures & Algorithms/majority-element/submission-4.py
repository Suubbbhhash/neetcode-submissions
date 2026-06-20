from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic=Counter(nums)
        res=max(dic,key=dic.get)
        return res
