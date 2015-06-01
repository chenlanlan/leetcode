#!/usr/bin/python

class Solution:
    # @param {character[][]} board
    # @param {string[]} words
    # @return {string[]}
    def isInBoard(self, x, y, board):
        if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]):
            return False
        return True
    
    def findWords(self, board, words):
        row, col = len(board), len(board[0])
        trie = Trie()
        for word in words:
            trie.insert(word)
        visit = [[False] * col for x in range(row)]
        dz = zip([1, 0, -1, 0], [0, 1, 0, -1])
        ans = []
        def dfs(word, node, x, y):
            node = node.childs.get(board[x][y])
            if node is None:
                return
            visit[x][y] = True
            for z in dz:
                nx, ny = x + z[0], y + z[1]
                if self.isInBoard(nx, ny, board) and not visit[nx][ny]:
                    dfs(word + board[nx][ny], node, nx, ny)
            if node.isWord:
                ans.append(word)
                trie.delete(word)
            visit[x][y] = False
        for x in range(row):
            for y in range(col):
                dfs(board[x][y], trie.root, x, y)
        return sorted(ans)

class TrieNode:
    def __init__(self):
        self.childs = dict()
        self.isWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for letter in word:
            child = node.childs.get(letter)
            if child is None:
                child = TrieNode()
                node.childs[letter] = child
            node = child
        node.isWord = True

    def delete(self, word):
        node = self.root
        queue = []
        for letter in word:
            queue.append((letter, node))
            child = node.childs.get(letter)
            if child is None:
                return False
            node = child
        if not node.isWord:
            return False
        if len(node.childs):
            node.isWord = False
        else:
            for letter, node in reversed(queuq):
                del node.childs[letter]
                if len(node.childs) or node.isWords:
                    break
        return True

test = Solution()
print(test.findWords([
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
], ["oath","pea","eat","rain"]))
