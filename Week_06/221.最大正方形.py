#
# @lc app=leetcode.cn id=221 lang=python3
#
# [221] 最大正方形
#
# dp[i][j]表示以(i,j)为右下角，只包含1的最大边长值
# @lc code=start
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m  = len(matrix)
        if m == 0: return 0
        n = len(matrix[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        max_slide = 0
        for i in range(m):
            for j in range(n):
                # 当前值为1
                if matrix[i][j] == '1':
                    # 不跟其他元素构成正方形
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        # 左、左上、上的dp值+1
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                max_slide = max(max_slide, dp[i][j])
        return max_slide * max_slide
# @lc code=end

