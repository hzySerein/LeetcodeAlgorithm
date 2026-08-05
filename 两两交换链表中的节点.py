class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head

        p = head
        new_start = p.next
        while True:
            q = p.next
            temp = q.next

            q.next = p
            if not temp or not temp.next:
                p.next = temp
                break
            p.next = temp.next
            p = temp

        return new_start


        


        