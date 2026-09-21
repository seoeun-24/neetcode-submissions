class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #ok so take the target number using nums. 
        #return the index number.
        
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    return [i,j]
                
                

                


