#!/usr/bin/python

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} k
    # @return {ListNode}
    def rotateRight(self, head, k):
        if head == None or head.next == None or k == 0:
            return head
        p = head
        n = 1
        while p.next != None:
            n += 1
            p = p.next
        q = head
        q_step = 1
        if k % n == 0:
            return head
        while q_step < n - k % n:
            q_step += 1
            q = q.next
        start = q.next
        q.next = None
        p.next = head
        return start
            
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

Lists = MyClass.numsToLinkedList([1, 2])
test = Solution()
ans = test.rotateRight(Lists, 3)
MyClass.printLinkedList(ans)
