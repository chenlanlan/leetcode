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
    def needReverse(self, node, k):
        n = node
        count = 0
        while n != None:
            count += 1
            n = n.next
        if count < k: return False
        else: return True

    def reverseGroup(self, pre, nNode, k):
        startNode = nNode
        postNode = nNode.next
        for i in range(k - 1):
            if postNode == None:
                return None
            temp = postNode.next
            postNode.next = nNode
            nNode = postNode
            postNode = temp
        pre.next = nNode
        startNode.next = postNode
        return startNode

    def reverse(self, pre, node, k):
        if self.needReverse(node, k):
            nextPre = self.reverseGroup( pre, node, k)
            self.reverse(nextPre, nextPre.next, k)
        return
        
    def reverseKGroup(self, head, k):
        p = ListNode(0)
        pre = p
        p.next = head
        self.reverse(p, p.next, k)
        return pre.next
    
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

Lists = MyClass.numsToLinkedList([1, 2, 3, 4, 5])
test = Solution()
result = test.reverseKGroup(Lists, 3)
MyClass.printLinkedList(result)            
            
