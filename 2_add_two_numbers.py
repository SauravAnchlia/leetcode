# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = head = ListNode(0)
        carry = 0 
        while l1 or l2 or carry:
            print(f'l1 {l1.val}')
            print(f'l2 {l2.val}')
            print(f'carry {carry}')
            if l1:
                carry+= l1.val
                l1 = l1.next 
            if l2:
                carry+=l2.val
                l2=l2.next
            carry, rem = divmod(carry,10)
            head.next = ListNode(rem)
            head = head.next 
        return root.next 



    def generate_linked_list(self, num : str)->ListNode:
        root = head  = ListNode(0)
        for char in num[::-1]:
            some_ll = ListNode(int(char))
            head.next = some_ll
            head = some_ll
        return root 




obj = Solution()
l1 = obj.generate_linked_list('123')
l2 = obj.generate_linked_list('123')
obj.addTwoNumbers(l1,l2)

