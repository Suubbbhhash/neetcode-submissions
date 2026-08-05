class Solution:
    def tribonacci(self, n: int) -> int:
        if n==0:
            return 0
        n+=1
        res = [0, 1, 1] + [0] * (n - 3)

        for i in range(3, n):
            res[i] = res[i-1] + res[i-2] + res[i-3]

        return res[-1] 