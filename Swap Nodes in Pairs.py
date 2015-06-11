#!/usr/bin/python

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def swapPairs(self, head):
        pre = root = ListNode(0)
        pre.next = head
        if head == None or head.next == None:
            return head
        fast = head.next
        slow = head
        while fast:
            next = fast.next
            fast.next = slow
            slow.next = next
            pre.next = fast
            pre = slow
            if next:
                fast = next.next
                slow = next
            else:
                break
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

Lists = MyClass.numsToLinkedList([1, 2, 3, 4, 5, 6, 7])
test = Solution()
result = test.swapPairs(Lists)
MyClass.printLinkedList(result)
            
        
            
        
        
