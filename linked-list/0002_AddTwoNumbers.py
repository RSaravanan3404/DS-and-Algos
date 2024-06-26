from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy = ListNode()
        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val % 10 if l1 else 0
            v2 = l2.val % 10 if l2 else 0
            v = v1 + v2 + carry
            carry = v // 10
            v = v % 10
            cur.next = ListNode(v)
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next
    

link = "https://leetcode.com/problems/add-two-numbers/"
