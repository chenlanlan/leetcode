# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def insertionSortList2(self, head):
        if not head:
            return None
        dummy = ListNode(0)
        dummy.next = head
        cur = head
        while cur.next:
            if cur.next.val < cur.val:
                pre = dummy
                while pre.next.val < cur.next.val:
                    pre = pre.next
                temp = cur.next
                cur.next = temp.next
                temp.next = pre.next
                pre.next = temp
            else:
                cur = cur.next
        self.printList(dummy.next)
        return dummy.next
    
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
print(test.insertionSortList2(head))