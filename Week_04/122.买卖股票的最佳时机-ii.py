#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
from typing import List
# 动态规划、贪心算法
# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 贪心算法
        # res = []
        # for i in range(1, len(prices)):
        #     if prices[i] > prices[i - 1]: 
        #         res.append(prices[i]-prices[i-1])
        # return sum(res)
        
        # # 动态规划
        # # dp[i][0] 第 i 天交易完后手里没有股票的最大利润
        # # dp[i][1] 第 i 天交易完后手里有股票的最大利润
        # dp = [[0]*2]*len(prices)
        # dp[0][0], dp[0][1] = 0, -prices[0]
        # for i in range(1, len(prices)):
        #     # i-1天手里没股票，或i-1天手里有股票但是立即卖出（+prices[i])的最大值
        #     dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
        #     # i-1天手里有股票，或i-1天手里没股票但是买入了的最大值
        #     dp[i][1] = max(dp[i-1][1], dp[i-1][0]-prices[i])

        # # 最终手里没股票的收益大于手里有股票的
        # return dp[len(prices)-1][0]

        # 稍微改良，只用记录前一天的值
        dp0, dp1 = 0, -prices[0]
        for i in range(1, len(prices)):
            dp0 = max(dp0, dp1 + prices[i])
            dp1 = max(dp1, dp0 - prices[i])
        return dp0
# @lc code=end
Solution().maxProfit([7,1,5,3,6,4])
