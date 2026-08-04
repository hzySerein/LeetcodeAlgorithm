class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        res = ListNode()
        current = res
        
        p, q = list1, list2
        
        while p and q:
            if p.val <= q.val:
                current.next = p
                p = p.next
            else:
                current.next = q
                q = q.next
            current = current.next
        

        if p:
            current.next = p
        if q:
            current.next = q
        
        return res.next