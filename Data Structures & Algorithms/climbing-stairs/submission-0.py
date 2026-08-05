class Solution:
    def climbStairs(self, n: int) -> int:
        sqrt5=math.sqrt(5)
        a=(1+sqrt5)/2
        b=(1-sqrt5)/2
        n+=1
        return round((a**n-b**n)/sqrt5)