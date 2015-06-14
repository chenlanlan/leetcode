class Solution:
    # @param beginWord, a string
    # @param endWord, a string
    # @param wordDict, a set<string>
    # @return an integer
    def edit(self, word):
        alphabet =  'abcdefghijklmnopqrstuvwxyz'
        splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
        replaces = [a + c + b[1:] for a, b in splits for c in alphabet if b]
        #print(replaces)
        replaces.remove(word)
        return replaces
    
    def ladderLength(self, beginWord, endWord, wordDict):
        currQueue = []
        currQueue.append(beginWord)
        if endWord not in wordDict:
            wordDict.append(endWord)
        if beginWord in wordDict:
            wordDict.remove(beginWord)
        ret = 0
        while True:
            ret += 1
            nextQueue = []
            while len(currQueue):
                s = currQueue.pop(0)
                if s == endWord:
                    return ret
                editWords = self.edit(s)
                for word in editWords:
                    if word in wordDict:
                        wordDict.remove(word)
                        nextQueue.append(word)
            if len(nextQueue) == 0:
                return 0
            currQueue = nextQueue
        return 0

test = Solution()
print(test.ladderLength("hit", 'cog', ["hot","dot","dog","lot","log"]))
