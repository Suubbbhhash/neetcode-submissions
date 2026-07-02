class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k==0:
            return False
        for i in range (len(nums)-1):
            for j in range (i+1,len(nums)):
                if nums[i]==nums[j]:
                    if abs(i-j)<=k:
                        return True
        return False