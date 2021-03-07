#
# @lc app=leetcode.cn id=32 lang=python3
#
# [32] 最长有效括号
#
# 动态规划
# dp[i]表示直到s[i]最长有效括号
# 状态转移：
# dp[i] = dp[i-2] + 2
# 
# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # 动态规划
        # max_ans = 0
        # dp = [0 for _ in range(len(s))]
        # for i in range(len(s)):
        #     # 只有当前s[i]==')'时有效括号的个数才会增加
        #     if s[i] == ')' and i > 0:
        #         if s[i-1] == '(':
        #             dp[i] = dp[i-2] + 2
        #         # '))'的情况，需要判断前一个')'是否有对应的成对括号
        #         elif i - dp[i-1] > 0 and s[i-dp[i-1]-1] == '(':
        #             # i−dp[i−1]−1 和 i组成了有效括号对,还需要多加dp[i-dp[i-1]-2]
        #             if i - dp[i] >= 2:
        #                 dp[i] = dp[i-1] + dp[i-dp[i-1]-2] + 2 
        #             else:
        #                 dp[i] = dp[i-1] + 2
        #         max_ans = max(max_ans, dp[i])
        # return max_ans

        # 栈
        max_ans = 0
        stack = [-1]
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif len(stack) > 1:
                stack.pop()
                max_ans = max(max_ans, i-stack[-1])
            else:
                # 边界
                stack[0] = i
        return max_ans

# @lc code=end
print(Solution().longestValidParentheses("()"))