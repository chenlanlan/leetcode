#!/usr/bin/python

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def sortList(self, head):
        if head == None or head.next == None:
            return head
        mid = self.getMid(head)
        secondPart = None
        if mid:
            secondPart = mid.next
            mid.next = None
        list1 = self.sortList(head)
        list2 = self.sortList(secondPart)
        listSorted = self.mergeLists(list1, list2)
        return listSorted
        
    #get the middle node of the list
    def getMid(self, node):
        if node == None or node.next == None:
            return node
        slow = node
        fast = node.next
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
        return slow

    # merge two sorted lists into one sorted list
    def mergeLists(self, node1, node2):
        if node1 == None:
            return node2
        if node2 == None:
            return node1
        res = ListNode(0)
        cur = res
        while node1 and node2:
            if node1.val < node2.val:
                cur.next = node1
                node1 = node1.next
            else:
                cur.next = node2
                node2 = node2.next
            cur = cur.next
        if node1:
            cur.next = node1
        if node2:
            cur.next = node2
        return res.next

class TestUtil():
    def printLinkedList(self, head):
        while head != None:
            print(head.val)
            head = head.next
        return
    
    def numsToLinkedList(self, nums):
        res = ListNode(0)
        cur = res
        for num in nums:
            node = ListNode(num)
            cur.next = node
            cur = cur.next
        return res.next
    
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

Lists = MyClass.numsToLinkedList([1, 2, 3])
MyClass.printLinkedList(Lists)

print('---')
test = TestUtil()
head = test.numsToLinkedList([5, 9, 5, 3, 6, 2, 4, 1])        

test_res = Solution()
result = test_res.sortList(head)
test.printLinkedList(result)
            
                
            
