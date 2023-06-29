class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        DIRS = [[-1,0],[1,0],[0,1],[0,-1]]
        grid = [list(row) for row in grid]

        start = (0, 0)
        K = 0 # total keys
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]=='@': start = (r, c)
                if grid[r][c].islower(): K += 1

        self.ans = inf
        def bfs(r, c, keys, totalSteps):
            queue = deque([(r, c, totalSteps)])
            visit = {}
            while queue:
                r, c, s = queue.popleft()
                if (r, c) in visit and visit[(r, c)]<=s: continue
                visit[(r, c)] = s
                
                if grid[r][c].islower():
                    key = grid[r][c]
                    keys[key] = (r, c, s)
                    grid[r][c] = '.'
                    if len(keys)==K:
                        self.ans = min(self.ans, s)
                    else:
                        bfs(r, c, keys, s)
                    grid[r][c] = key
                    del keys[key]
                    continue
                
                for dr, dc in DIRS:
                    rr, cc = r+dr, c+dc
                    if 0<=rr<ROWS and 0<=cc<COLS:
                        cell = grid[rr][cc]
                        if cell=='@' or cell=='.' or cell.islower() or cell.lower() in keys:
                            queue.append((rr, cc, s+1))
            return keys

        bfs(start[0], start[1], {}, 0)
        if self.ans==inf: return -1
        return self.ans