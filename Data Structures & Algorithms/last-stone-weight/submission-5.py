class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        if len(stones)==1:
            return stones[0]
        if len(stones)==0:
            return 0
        else:
            x=stones.pop()
            y=stones.pop()
            if x==y:
                return self.lastStoneWeight(stones)
            if x>y:
                stones.append(x-y)
                return self.lastStoneWeight(stones)    