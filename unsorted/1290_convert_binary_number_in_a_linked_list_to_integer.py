'''
description:
Given head, which is a reference node to a singly linked list. The value of each node in the linked list is either 0 or 1.
The linked list holds the binary representation of a number 
'''


class solution:
    def getDecimalValue(self, head: ListNode) -> int:
        num = 0
        while head:
            num = num << 1
            num = num | head.val
            head = head.next
        return num
