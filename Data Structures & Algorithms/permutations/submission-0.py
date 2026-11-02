class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        #should return n! subsets
        path,res=[],[]
        def backtracking():
            if len(path)==len(nums):               # 힌트 3
                res.append(path[:])
                return

            for i in range(len(nums)):
                if nums[i] in path:           # 힌트 2: 이미 쓴 원소면 건너뜀
                    continue
                path.append(nums[i])
                backtracking()
                path.pop()

        # 고른다 (path에 추가, 사용 표시)
        backtracking()
        # 되돌린다 (path에서 제거, 사용 표시 해제)
        return res