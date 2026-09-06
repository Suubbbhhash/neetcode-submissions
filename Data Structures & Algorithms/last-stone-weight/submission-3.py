class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones)>1:
            a=max(stones)
            stones.remove(a)
            b=max(stones)
            stones.remove(b)
            if a==b:
                continue
            else:
                stones.append(abs(a-b))
        if len(stones)==1:
            return stones[0]
        else:
            return 0