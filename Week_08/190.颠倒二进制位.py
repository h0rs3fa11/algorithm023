#
# @lc app=leetcode.cn id=190 lang=python3
#
# [190] 颠倒二进制位
#

# @lc code=start
class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for _ in range(32):
            # 上一个结果位左移
            res <<= 1
            # 取n最后一位放到res最后
            res |= n & 1
            # n右移
            n >>= 1
        return res
# @lc code=end

