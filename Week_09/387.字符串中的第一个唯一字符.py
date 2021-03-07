#
# @lc app=leetcode.cn id=387 lang=python3
#
# [387] 字符串中的第一个唯一字符
#
import collections
# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:
        # # 哈希表 计数
        # if len(s) == 0:
        #     return -1
        # count = collections.Counter(s)
        # for key, value in count.items():
        #     if value == 1:
        #         return s.index(key)
        # return -1

        # 队列
        m = dict()
        queue = collections.deque()
        for i, v in enumerate(s):
            if v not in m:
                m[v] = i
                queue.append((v, i))
            else:
                m[v] = -1
                while queue and m[queue[0][0]] == -1:
                    queue.popleft()
        return -1 if not queue else queue[0][1]
# @lc code=end

