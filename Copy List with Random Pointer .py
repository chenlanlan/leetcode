# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
def copyRandomList(self, head):
    if not head: return None
    result = None
    pOld = head
    pNew = result
    while pOld:
        pOldNext = pOld.next
        pNew = RandomListNode(pOld.label)
        pOld.next = pNew
        pNew.next = pOldNext
        if result == None:
            result = pNew
        pOld = pOldNext
    pOld = head
    while pOld:
        if pOld.random:
            pOld.next.random = pOld.random.next
        pOld = pOld.next.next
    pOld = head
    pNew = result
    while pNew.next:
        pOld.next = pNew.next
        pOld = pOld.next
        pNew.next = pOld.next
        pNew = pNew.next
    pOld.next = None
    pNew.next = None
    return result