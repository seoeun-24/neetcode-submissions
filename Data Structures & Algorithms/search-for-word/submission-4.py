class Solution:
    def exist(self, board, word):
        rows, cols = len(board), len(board[0])

        def backtracking(r, c, k):
            if k == len(word):
                return True
            if (r < 0 or r >= rows or c < 0 or c >= cols
                    or board[r][c] != word[k]):
                return False

            temp = board[r][c]
            board[r][c] = '#'
            found = (backtracking(r + 1, c, k + 1) or
                     backtracking(r - 1, c, k + 1) or
                     backtracking(r, c + 1, k + 1) or
                     backtracking(r, c - 1, k + 1))
            board[r][c] = temp
            return found

        for r in range(rows):
            for c in range(cols):
                if backtracking(r, c, 0):
                    return True
        return False
        