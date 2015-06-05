#!/usr/bin/python

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        A, B = headA, headB
        countA, countB = 0, 0
        while A:
            A = A.next
            countA += 1
        while B:
            B = B.next
            countB += 1
        if countA < countB:
            count = 0
            while count < countB - countA:
                headB = headB.next
                count += 1
        elif countA > countB:
            count = 0
            while count < countA - countB:
                headA = headA.next
                count += 1
        while headA and headB:
            if headA.val == headB.val:
                return headA
            else:
                headA = headA.next
                headB = headB.next
        return
            
        
