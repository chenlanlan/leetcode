#!/usr/bin/python

#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} k
    # @return {ListNode}
    def reverseGroup(self, beginPre, begin, end):
        endNext = end.next
        pre = begin
        cur = begin.next
        while cur != endNext:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        begin.next = endNext
        beginPre.next = end
        return begin
        
    def reverseKGroup(self, head, k):
        headPre = ListNode(0)
        headPre.next = head
        pre = headPre
        p = head
        while p != None:
            begin = p; end = p
            i = 0
            while i < k - 1 and end:
                end = end.next
                i += 1
            if end == None: break
            pre = self.reverseGroup(pre, begin, end)
            p = pre.next
        return headPre.next
            
class MyClass(object):
    @staticmethod
    def printLinkedList(head):
        while head != None:
            print(head.val)
            head = head.next
        return
    
    def numsToLinkedList(nums):
        res = ListNode(0)
        cur = res
        for num in nums:
            node = ListNode(num)
            cur.next = node
            cur = cur.next
        return res.next

Lists = MyClass.numsToLinkedList([1, 2, 3, 4, 5, 6])
test = Solution()
result = test.reverseKGroup(Lists, 3)
MyClass.printLinkedList(result)            
            
