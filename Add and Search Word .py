class TrieNode:
    def __init__(self):
        self.childs = dict()
        self.isWord = False

class WordDictionary:
    # initialize your data structure here.
    def __init__(self):
        self.root = TrieNode()
    
    # @param {string} word
    # @return {void}
    # Adds a word into the data structure.
    def addWord(self, word):
        node = self.root
        for letter in word:
            child = node.childs.get(letter)
            if child is None:
                child = TrieNode()
                node.childs[letter] = child
            node = child
        node.isWord = True
    
    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the data structure. A word could
    # contain the dot character '.' to represent any one letter.
    def search(self, word):
        return self.searchdeep(word, 0, self.root)
    
    def searchdeep(self, word, idx, node):
        if node.childs == {} or idx >= len(word):
            return False
        for i in range(idx, len(word)):
            if word[i] == '.' and i < len(word) - 1:
                for letter in node.childs:
                    if self.searchdeep(word, i + 1, node.childs[letter]):
                        return True
                return False
            elif word[i] == '.' and i == len(word) - 1:
                for letter in node.childs:
                    if node.childs[letter].isWord:
                        return True
                return False
            else:
                node = node.childs.get(word[i])
                if node is None:
                    return False
    return node.isWord

WordDictionary = WordDictionary()
WordDictionary.addWord('bad')
print(WordDictionary.search('b..'))