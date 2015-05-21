#!/usr/bin/python

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} x
    # @return {ListNode}
    def partition(self, head, x):
        p, q = ListNode(0), ListNode(0) #p represents nodes value >= x
        p.next, q.next = head, head
        while p.next and p.next.val < x:
            q = q.next
            p = p.next
        while p.next != None:
            if p.next.val >= x:
                p = p.next
                continue
            start = q.next
            temp = p.next.next
            newStart = p
            p.next.next = q.next
            q.next = p.next
            newStart.next = temp
            if start == head:
                head = q.next 
            q = q.next
            p = newStart              
        return head
    
    def partition2(self, head, x):
        p, q = ListNode(0), ListNode(0)
        pStart = p
        qStart = q
        h = head
        while h != None:
            if h.val < x:
                q.next = h
                q = q.next
            else:
                p.next = h
                p = p.next
            h = h.next
        p.next = None
        q.next = pStart.next
        return qStart.next
        
            
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

Lists = MyClass.numsToLinkedList([4, 3, 2, 5])
test = Solution()
MyClass.printLinkedList(test.partition(Lists, 3))            
            
            
            
                
        
        
