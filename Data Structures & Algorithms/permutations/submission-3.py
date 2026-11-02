class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        path,res=[],[]

        def backtracking():
            if len(path)==len(nums):
                res.append(path[:])
                return
            for i in range(len(nums)):
                if nums[i] not in path:
                    path.append(nums[i])
                    backtracking()
                    path.pop()

        backtracking()
        return res


            
        