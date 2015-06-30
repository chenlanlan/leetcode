class Solution:
    # @param {string} word1
    # @param {string} word2
    # @return {integer}
    def minDistance(self, word1, word2):
        m = len(word1)
        n = len(word2)
        d = [[0 for i in range(n + 1)] for j in range(m + 1)]
        for i in range(m + 1):
            d[i][0] = i
        for i in range(n + 1):
            d[0][i] = i
        for j in range(1, n + 1):
            for i in range(1, m + 1):
                if word1[i - 1] == word2[j - 1]:
                    d[i][j] = d[i - 1][j - 1]
                else:
                    d[i][j] = min(d[i - 1][j], d[i][j - 1], d[i - 1][j - 1]) + 1
        print (d)
        return d[m][n]

test = Solution()
print(test.minDistance('', ''))