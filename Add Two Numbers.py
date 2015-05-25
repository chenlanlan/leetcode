#!/usr/bin/python

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def addTwoNumbers(self, l1, l2):
        root = ListNode(0)        
        re = 0
        ansNode = root
        while l1 or l2:
            if l1:
                num1 = l1.val
            else:
                num1 = 0
            if l2:
                num2 = l2.val
            else:
                num2 = 0
            sum = num1 + num2 + re
            value = sum % 10
            ansNode.next = ListNode(value)
            re = sum // 10
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            ansNode = ansNode.next
        if re > 0:
            ansNode.next = ListNode(re)
        return root.next
    
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

l1 = MyClass.numsToLinkedList([1, 2, 3, 6])
l2 = MyClass.numsToLinkedList([3, 4, 8, 6])
test = Solution()
result = test.addTwoNumbers(l1, l2)
MyClass.printLinkedList(result)

            
            
    
