#!/usr/bin/python

class Solution:
    # @param {ListNode} head
    # @param {integer} m
    # @param {integer} n
    # @return {ListNode}
    def reverseBetween(self, head, m, n):
        if head == None or head.next == None or m == n:
            return head
        p1 = head
        count = 1
        length = n - m + 1
        if m == 1:
            p1 = head
            p2, p3 = head.next, head.next
            while count < length:
                p3 = p2.next
                p2.next = p1
                p1 = p2
                p2 = p3
                count += 1
            head.next = p2
            return p1
        else:
            while count < m - 1:
                p1 = p1.next
                count += 1
            count = 1
            preStart = p1
            start = p1.next
            p1 = p1.next
            p2 = p1.next
            p3 = p2
            while count < length:
                p3 = p2.next
                p2.next = p1
                p1 = p2
                p2 = p3
                count += 1
            preStart.next = p1
            start.next = p2
            return head
        
    def reverseBetween2(self, head, m, n):
        if head == None or head.next == None or m == n:
            return head
        p1 = head
        preStart = None
        count = 1
        while count < m:
            preStart = p1
            p1 = p1.next
            count += 1
        p2 = p1.next
        p3 = p2
        start = p1
        count = 1
        length = n - m + 1
        while count < length:
                p3 = p2.next
                p2.next = p1
                p1 = p2
                p2 = p3
                count += 1
        start.next = p2
        if preStart:
            preStart.next = p1
        else:
            head = p1
        return head
        
        

            
