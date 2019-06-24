import collections
class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for letter in word:
            current = current.children[letter]
        current.isWord = True
    
    def search(self, word):
        current = self.root
        for letter in word:
            current = current.children.get(letter)
            if not current: return False
        return current.isWord

class Solution:
    def findWords(self, board, words):

        res = []
        trie = Trie()
        node = trie.root
        for word in words:
            trie.insert(word)
        
        def backtrack(node, row, col, path):
            if node.isWord:
                res.append(path)
                node.isWord = False
            
            if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
                return 

            tmp = board[row][col]
            node = node.children.get(tmp)
            if not node: return
            
            board[row][col] = '#'
            backtrack(node, row + 1, col, path + tmp)
            backtrack(node, row - 1, col, path + tmp)
            backtrack(node, row, col + 1, path + tmp)
            backtrack(node, row, col - 1, path + tmp)
            board[row][col] = tmp
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                backtrack(node, i, j, "")

        return res