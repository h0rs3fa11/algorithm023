#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
from typing import List
# dfs bfs
# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # def dfs(r, c):
        #     # 标记为0
        #     grid[r][c] = 0
        #     nr, nc = len(grid), len(grid[0])
        #     # 周围的点
        #     for x, y in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
        #         # 如果x,y在范围内并且点是1，继续遍历
        #         if 0 <= x < nr and 0 <= y < nc and grid[x][y] == '1':
        #             dfs(x, y)
        # nr = len(grid)
        # if nr == 0: return 0
        # nc = len(grid[0])
        
        # num_island = 0
        # for r in range(nr):
        #     for c in range(nc):
        #         if grid[r][c] == '1':
        #             num_island += 1
        #             dfs(r, c)
        # return num_island

        # # bfs
        # from collections import deque
        # nr = len(grid)
        # if nr == 0:
        #     return 0
        # nc = len(grid[0])

        # num_islands = 0
        # for r in range(nr):
        #     for c in range(nc):
        #         if grid[r][c] == '1':
        #             num_islands += 1
        #             grid[r][c] = '0'
        #             nebors = deque([(r, c)])
        #             while nebors:
        #                 row, col = nebors.popleft()
        #                 for x, y in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:
        #                     if 0 <= x < nr and 0 <= y < nc and grid[x][y] == '1':
        #                         nebors.append((x, y))
        #                         grid[x][y] = '0'
        # return num_islands

        # 大佬写的dfs
        def sink(i, j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == '1':
                grid[i][j] = '0'
                list(map(sink, (i + 1, i - 1, i, i), (j, j, j + 1, j - 1)))
                return 1
            return 0
        return sum(sink(i, j) for i in range(len(grid)) for j in range(len(grid[i])))
# @lc code=end
grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
print(Solution().numIslands(grid))
