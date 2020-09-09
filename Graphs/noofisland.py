#https://leetcode.com/problems/number-of-islands/
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        For every land, visit its neighborland
        using DFS until there's no such land mark every visited nodes to 0
        """

        # initialization
        m = len(grid)
        if m == 0: return 0
        n = len(grid[0])
        ans = 0

        for y in range(m):
            for x in range(n):
                if grid[y][x] == '1':
                    ans += 1
                    self.dfs(grid, x, y, m, n)
        return ans

    def dfs(self, grid, x, y, m, n):
        if x < 0 or y < 0 or x >= n or y >= m or grid[y][x] == '0':
            return None
        grid[y][x] = '0'
        self.dfs(grid, x + 1, y, m, n)
        self.dfs(grid, x - 1, y, m, n)
        self.dfs(grid, x, y - 1, m, n)
        self.dfs(grid, x, y + 1, m, n)
