from representation import ListNode, head
from typing import Optional

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1

        ind = length - n
        curr = head

        if ind == 0:
            head = head.next
            curr.next = None
            return head

        for _ in range(ind-1):
            curr = curr.next

        curr.next = curr.next.next
        return head
    

obj = Solution()
obj.removeNthFromEnd(head, int(input()))