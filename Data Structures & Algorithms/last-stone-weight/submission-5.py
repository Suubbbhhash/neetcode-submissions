class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones)>1:
            stones.sort()
            a=stones[-1]
            stones.pop()
            b=stones[-1]
            stones.pop()
            if a==b:
                continue
            else:
                stones.append(abs(a-b))
        if len(stones)==1:
            return stones[0]
        else:
            return 0