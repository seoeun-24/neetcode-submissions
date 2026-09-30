class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
          
        res={}
        for num in nums:
            if num in res:
                return num

            res[num]=1

    """res = {}
        for num in nums:
            if num in res:
                res[num] += 1
            else:
                res[num] = 1

        if res[num] != 1:
            return num
            => this is not correct, out of the loop res[num], it only handles the last element which is 4 in example 2.not dealing with all num in nums.

            so here i can fix like this

        res = {}
        for num in nums:
            if num in res:
                res[num] += 1
            else:
                res[num] = 1

        return max(res, key=res.get) 
        => key=res.get plays read how many times the number appeared in dictionary and max(res,key-res.get)return the most frequent number appeared in dictionary.
    """
           
        
