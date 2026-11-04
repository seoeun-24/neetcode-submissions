class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res,path=[],[]

        def backtracking(start, remaining):
            if remaining==0:
                res.append(path[:])
                return
            
            for i in range(start,len(candidates)):
                if start<i and candidates[i]==candidates[i-1]:
                    continue
                if candidates[i]>remaining:
                    break
                
                path.append(candidates[i])
                backtracking(i+1,remaining-candidates[i])
                path.pop()
        backtracking(0,target)
        return res