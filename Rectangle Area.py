class Solution:
    # @param {integer} A
    # @param {integer} B
    # @param {integer} C
    # @param {integer} D
    # @param {integer} E
    # @param {integer} F
    # @param {integer} G
    # @param {integer} H
    # @return {integer}
    def commonRange(self, Astart, Aend, Bstart, Bend):
        if Astart >= Bend or Aend <= Bstart:
            return [0, 0]
        resStart = max(Astart, Bstart)
        resEnd = min(Bend, Aend)
        return [resStart, resEnd]
        
    def computeArea(self, A, B, C, D, E, F, G, H):
        areaABCD = abs(A - C) * abs(B - D)
        areaEFGH = abs(E - G) * abs(F - H)
        Length = self.commonRange(A, C, E, G)
        Breadth = self.commonRange(B, D, F, H)       
        DupAreaLength = Length[1] - Length[0]
        DupAreaBreadth = Breadth[1] - Breadth[0]
        DupArea = DupAreaLength * DupAreaBreadth
        area = areaABCD +areaEFGH - DupArea
        return area
    
test = Solution()
print(test.commonRange(4, 7, 1, 5))
print(test.computeArea(0, 0, 0, 0, -1, -1, 1, 1))
