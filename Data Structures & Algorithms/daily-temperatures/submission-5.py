class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        new=[]

        res = [0]* len(temperatures)
        
        for i in range(len(temperatures)):
            while new and temperatures[i]>temperatures[new[-1]]:
                prev= new.pop()
                res[prev]=i-prev
            new.append(i)

        return res



