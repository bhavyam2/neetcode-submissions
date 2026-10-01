from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(0,1), (0,-1), (-1,0), (1,0)]
        row, col = len(grid), len(grid[0])
        answer = 0
        def bfs(r, c):
            q = deque([(r,c)])
            while q:
                ro, co = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr + ro, dc + co
                    if (nr < 0 or nc < 0 or nr >= row or nc >= col or grid[nr][nc] == "0"):
                        continue
                    q.append((nr,nc))
                    grid[nr][nc] = "0"

        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1":
                    bfs(r,c)
                    answer += 1
        
        return answer


        
