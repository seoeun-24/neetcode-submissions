class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        from collections import deque

        ROWS, COLS = len(grid), len(grid[0])
        q = deque()

        # 1. Find all treasure chests (gates)
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))

        # 2. BFS
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q:
            r, c = q.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                # Check boundaries and whether it is land
                if (nr < 0 or nr >= ROWS or
                    nc < 0 or nc >= COLS or
                    grid[nr][nc] != 2147483647):
                    continue

                grid[nr][nc] = grid[r][c] + 1
                q.append((nr, nc))
