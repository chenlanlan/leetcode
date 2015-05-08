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
        node = head
        sortHead = head
        A = []
        while head != None:
            A.append(head.val)
            head = head.next
        A = self.quickSort(A)
        print(A)
        i = 0
        while sortHead != None:
            sortHead.val = A[i]
            sortHead = sortHead.next
            i += 1
        self.printList(node)
        return node
        
    def quickSort(self, A):
        low = 0
        high = len(A) - 1
        def Sort(A, low, high):
            def partition(A, low, high):
                key = A[low]
                while low < high:
                    while A[high] >= key and low < high:
                        high -= 1
                    A[low], A[high] = A[high], A[low]
                    while A[low] <= key and low < high:
                        low += 1
                    A[low], A[high] = A[high], A[low]
                return low
            while low < high:
                P = partition(A, low, high)
                Sort(A, low, P - 1)
                Sort(A, P + 1, high)
                return A
        Sort(A, low, high)
        return A

    def printList(self, head):
        while head != None:
            print(head.val)
            head = head.next
        return

head = ListNode(5)
node2 = ListNode(3)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(1)
head.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
test = Solution()
print(test.sortList(head))
            
                
            
