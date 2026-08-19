class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if not head or not head.next or k ==0 :
            return head
        def len_list(head):
            l = 0
            while head:
                head = head.next
                l += 1

            return l

        l = len_list(head)
        k = k % l
        if k ==0 :
            return head 

        slow = head
        fast = head

        for i in range(k):
            fast = fast.next

        while fast.next:
            slow = slow.next
            fast = fast.next

        res = slow.next
        slow.next = None
        fast.next = head

        return res