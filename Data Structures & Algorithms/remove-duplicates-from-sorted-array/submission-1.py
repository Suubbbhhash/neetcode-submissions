from collections import Counter
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        dic=dict(Counter(nums))
        res=[]
        for key in dic.keys():
            res.append(key)
        for i in range(len(res)):
            nums[i]=res[i]
        return len(res)