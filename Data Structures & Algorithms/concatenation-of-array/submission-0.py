class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        res=[0]*2*len(nums)
        i=0
        while i<len(nums):
            res[i]=nums[i]
            res[len(nums)+i]=nums[i]
            i+=1
        return res



        