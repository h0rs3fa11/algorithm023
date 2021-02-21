#
# @lc app=leetcode.cn id=127 lang=python3
#
# [127] 单词接龙
#
# 建图 BFS
# 一种办法是O(N*len(wordList))，beginWord依次和其他所有单词比较，如果刚好差一位，说明可以转换
# 另一种办法是从a~z枚举beginWord所有位,如果结果在wordList中说明可以转换,O(26*len(wordList)) = O(len(wordList))

# 双端BFS
# 设置两个queue同时查找，每次优先查找较小的
# @lc code=start
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # # 1. 普通BFS
        # # 查找时间O(1)
        # word_set = set(wordList)
        # if len(word_set) == 0 or endWord not in word_set:
        #     return 0

        # if beginWord in word_set:
        #     word_set.remove(beginWord)
        # # 保存变化过程中在wordList内的单词
        # deque = collections.deque([beginWord])
        # # 访问过的单词
        # visited = set(beginWord)
        # word_len = len(beginWord)
        # step = 1

        # while deque:
        #     current = len(deque)
        #     # 遍历当前队列中的单词
        #     for _ in range(current):
        #         word = deque.popleft()
        #         # 单词转换为列表形式
        #         word_list = list(word)
        #         # 变换不同位上的字母
        #         for j in range(word_len):
        #             # 保存变化前字符
        #             origin = word_list[j]
        #             # a~z中变化
        #             for k in range(26):
                        #   string.lowercase
        #                 alpha = chr(ord('a') + k)
        #                 if alpha == origin:
        #                     continue
        #                 word_list[j] = alpha
        #                 new_word = ''.join(word_list)
        #                 # 如果新单词在wordList中，判断是否是endWord，如果不是判断是否被访问过（防止循环访问），添加到visited和即将访问的队列中
        #                 if new_word in word_set:
        #                     if new_word == endWord:
        #                         return step + 1
        #                     if new_word not in visited:
        #                         deque.append(new_word)
        #                         visited.add(new_word)
        #             word_list[j] = origin
        #     step += 1
        # return 0

        # 双端BFS
        word_set = set(wordList)
        if len(word_set) == 0 or endWord not in word_set:
            return 0
        if beginWord in word_set:
            word_set.remove(beginWord)
        
        begin_queue = collections.deque([beginWord])
        end_queue = collections.deque([endWord])
        word_len = len(beginWord)
        visited = set()
        step = 1

        while begin_queue:
            current = len(begin_queue)
            # 遍历当前的单词 
            for _ in range(current):
                word = begin_queue.popleft()
                for i in range(word_len):
                    for k in range(26):
                        c = chr(ord('a') + k)
                        if c == word[i]:
                            continue
                        new_word = word[:i] + c + word[i+1:]
                        if new_word in word_set:
                            if new_word in end_queue:
                                return step + 1
                            if new_word not in visited:
                                begin_queue.append(new_word)
                                visited.add(new_word)
            step += 1
            if len(begin_queue) > len(end_queue):
                end_queue, begin_queue = begin_queue, end_queue
        return 0
# @lc code=end

