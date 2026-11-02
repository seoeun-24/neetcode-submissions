class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        path,res=[],[]

        def backtracking(start):
            
            res.append(path[:])
            
            for i in range(start,len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                path.append(nums[i])
                backtracking(i+1)
                path.pop()
        nums.sort()
        backtracking(0)
        return res        

        