class Solution:
    def generateParenthesis(self, n):
        path, res = [], []

        def backtracking(opens, closes):
            if len(path) == 2 * n:
                res.append("".join(path))
                return
            if opens>closes:
                path.append(")")
                backtracking(opens,closes+1)
                path.pop()
            if opens<n:
                path.append("(")
                backtracking(opens+1,closes)
                path.pop()
        backtracking(0,0)
        return res
    

