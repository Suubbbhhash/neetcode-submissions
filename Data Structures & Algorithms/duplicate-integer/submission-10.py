from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        c=Counter(nums)
        for a,b in c.items():
            if b>1:
                return True
        return False