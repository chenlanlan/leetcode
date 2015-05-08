#!/usr/bin/python

def getIntersectionNode(self, headA, headB):
    if headA == None or headB == None:
        return None
    node = root = ListNode(0)
    node1 = headA
    node2 = headB
    count1 = count2 = 1
    while node1.next != None:
        count1 += 1
        node1 = node1.next
    while node2.next != None:
        count2 += 1
        node2 = node2.next
    if node1 != node2:
        return None
    else:
        count = abs(count1 - count2)
        if count1 < count2:
            node1 = headB
            node2 = headA
        else:
            node1 = headA
            node2 = headB
        while count > 0:
            node1 = node1.next
            count -= 1
        while node1 != None and node2 != None and node1 != node2:
            node1 = node1.next
            node2 = node2.next
        return node1
            
        
