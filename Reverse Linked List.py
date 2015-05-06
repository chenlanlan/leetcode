#!/user/bin/python

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        if head == None or head.next == None:
            return head
        res = ListNode(0)
        ans = res        
        while head.next != None:
            cur = head.next
            preCur = head
            while cur.next != None:
                cur = cur.next
                preCur = preCur.next
            res.next = cur
            res = res.next
            preCur.next = None
        res.next = head
        return ans.next

    def reverseList2(self, head):
        if head == None or head.next == None:
            return head
        p1 = head
        p2 = p1.next
        
        while p2:
            p3 = p2.next
            p2.next = p1
            p1 = p2
            p2 = p3   
        head.next = None
        return p1


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

Lists = MyClass.numsToLinkedList([1, 5, 6, 2, 3])
test = Solution()
#ans = test.reverseList(Lists)
ans2 = test.reverseList2(Lists)
#MyClass.printLinkedList(ans)
MyClass.printLinkedList(ans2)
