class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            a=x*(-1)
        else:
            a=x
        l=[int(s) for s in str(a)]
        r=l[::-1]
        t=int("".join(map(str,r)))
        if x<0:
            t=t*(-1)
        if t>(2**31 - 1) or t<(-2**31):
            return 0
        return t