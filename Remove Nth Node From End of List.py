#!/usr/bin/python

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        ans = ListNode(0)
        ans.next = head
        node = ans #两个指针，一个记录走的过程，一个记录走到每一步距离最后一步是否等于n
        temp = ans.next
        while node.next != None:
            i = 1
            while temp.next != None:
                temp = temp.next
                i += 1
            if i = n:
                node.next = node.next.next
                return ans.next
            else:
                node = node.next
                temp = node.next

#解法二
    def removeNthFromEnd2(self, head, n):
        ans = ListNode(0)
        ans.next = head
        first = ans #两个指针，一个先走n步，之后两个一起走，当第一个走到最后，第二个就是要删除的
        second = ans
        while n > 0:
            first = first.next
            n -= 1
        while first.next != None:
            first = first.next
            second = second.next
        second.next = second.next.next
        return ans.next
            
