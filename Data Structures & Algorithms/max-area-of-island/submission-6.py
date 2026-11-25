class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visit = set()
        rows, cols = len(grid), len(grid[0])

        def counting(r,c):
            if (r<0 or r>=rows or c<0 or c>= cols or grid[r][c]==0 or (r,c) in visit ):
                return 0
            visit.add((r,c))

            return (1+counting(r,c-1)
                    +counting(r,c+1)
                    +counting(r-1,c)
                    +counting(r+1,c))

        area =0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                area= max(area, counting(i,j))
        return area 
