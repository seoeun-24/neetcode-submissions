class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # if repeated return true

        new={}
        for num in nums:
            if num in new:
                return True
            else:
                new[num]=1

        return False

            

        

       


