class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        res = ListNode(0)
        p = res
        carry = 0

        while l1 and l2:
            sum = l1.val+l2.val+carry
            p.next = ListNode(sum%10)
            carry = sum//10
            l1 = l1.next
            l2 = l2.next
            p = p.next

        while l1:
            sum = l1.val+carry
            p.next = ListNode(sum%10)
            carry = sum//10
            l1 = l1.next
            p = p.next

        while l2:
            sum = l2.val+carry
            p.next = ListNode(sum%10)
            carry = sum//10
            l2 = l2.next
            p = p.next
        if carry ==1:
            p.next = ListNode(1)
        return res.next

 
