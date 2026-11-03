class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        if len(stones)==1:
            return stones[0]
        elif len(stones)==0:
            return 0
        else:
            x=stones.pop(-1)
            y=stones.pop(-1)
            if x==y:
                return self.lastStoneWeight(stones)
            elif x>y:
                stones.append(x-y)
                return self.lastStoneWeight(stones)
            
