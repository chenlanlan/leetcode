#!/user/bin/python

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):
        if head ==  None : 
            return
        middleNode = self.middleNode(head)
        if middleNode == None or middleNode.next == None:
            return 
        secondList = self.reverseList(middleNode.next)
        middleNode.next = None
        
        firstList = head
        while firstList != None and secondList != None:
            temp, temp2 = firstList.next, secondList.next
            firstList.next = secondList
            secondList.next = temp
            firstList = temp
            secondList = temp2   
        #self.printList(head)
        return
    
    def printList(self, head):
        while head != None:
            print(head.val)
            head = head.next
        return
            
    def middleNode(self, node):
        fast, slow = node, node
        while fast != None and fast.next != None: 
            fast = fast.next.next
            slow = slow.next
        return slow
    
    def reverseList(self, node):
        preNode = None
        while node != None:
            temp = node.next
            node.next = preNode
            preNode = node
            node = temp
        return preNode

head = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
head.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
test = Solution()
print(test.reorderList(head))
