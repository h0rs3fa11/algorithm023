#
# @lc app=leetcode.cn id=212 lang=python3
#
# [212] 单词搜索 II
#
# Trie树 + dfs回溯
# @lc code=start
import collections
from typing import List

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        self.board = board
        self.result = set()
        self.visited = set()
        for word in words:
            self.insert_word(word, root)
        self.m, self.n = len(board), len(board[0])
        for i in range(self.m):
            for j in range(self.n):
                if board[i][j] in root.children:
                    # 如果board中的当前元素在root.children内，就开始dfs
                    self.dfs(i, j, "", root)
        return list(self.result)

    def insert_word(self, word, root):
        node = root
        for c in word:
            node = node.children[c]
        node.end_of_word = True

    def dfs(self, x, y, cur_word, node):
        cur_word += self.board[x][y]
        cur_node = node.children[self.board[x][y]]
        if cur_node is not None and cur_node.end_of_word == True:
            self.result.add(cur_word)

        self.visited.add((x, y))

        for r, c in [(x+1, y), (x-1, y), (x, y-1), (x, y+1)]:
            if 0 <= r < self.m and 0 <= c < self.n and (r, c) not in self.visited and self.board[r][c] in cur_node.children and self.dfs(r, c, cur_word, cur_node):
                return True
        self.visited.remove((x, y))

class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.end_of_word = False

# @lc code=end
# board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
board = [["a","b"],["c","d"]]
# words = ["oath","pea","eat","rain"]
words = ["abcb"]
print(Solution().findWords(board, words))
