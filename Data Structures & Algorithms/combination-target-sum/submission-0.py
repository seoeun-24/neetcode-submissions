class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []

        def backtracking(start):
            if sum(path) > target:       # 넘으면 더 볼 필요 없음
                return
            if sum(path) == target:      # 합이 target이면 바로 기록
                res.append(path[:])
                return                   # (nums가 전부 양수라서 더 넣어도 합이 커질 뿐)
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtracking(i)          # i+1 이 아니라 i
                path.pop()

        backtracking(0)
        return res