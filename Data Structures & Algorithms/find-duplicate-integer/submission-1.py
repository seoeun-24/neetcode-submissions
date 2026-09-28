class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
          
        res={}
        for num in nums:
            if num in res:
                return num
            else:
                res[num]=1

    
           
        
