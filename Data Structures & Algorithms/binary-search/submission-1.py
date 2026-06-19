class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums) - 1
        if i > j:
            return -1
        m = (i + j) // 2
        if nums[m] > target:
            res = self.search(nums[i:m], target)
            return res if res == -1 else i + res
        elif nums[m] < target:
            res = self.search(nums[m+1:j+1], target)
            return res if res == -1 else m + 1 + res
        elif nums[m] == target:
            return m
        else:
            return -1