class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n=len(nums)
        t=[0]*n
        
        count=0
        for i in range(k):
            t[0]=nums[n-1]
            t[1:n]=nums[0:n-1]
            nums[:]=t[:]
        