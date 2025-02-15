# Question Link => https://leetcode.com/problems/number-of-islands/description/
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        
        rows = len(grid)
        cols = len(grid[0])

        count = 0
        visit = set()

        def bfs(r,c):
            q = deque()
            q.append((r,c))
            visit.add((r,c))
            while q:
                row,col = q.popleft()
                direction = [[1,0],[-1,0],[0,1],[0,-1]]
                for dr,dc in direction:
                    r = row + dr
                    c = col + dc
                    if(r in range(rows) and
                       c in range(cols) and
                        (r,c) not in visit and
                        grid[r][c] == "1"):
                        q.append((r,c))
                        visit.add((r,c))
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and((r,c) not in visit):
                    bfs(r,c)
                    count += 1
        return count                
