from representation import ListNode, head


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return
        if not head.next:
            return head
        prev = head
        node = head.next
        head.next = None

        while node.next:
            nxt = node.next
            node.next = prev
            prev = node
            node = nxt

        node.next = prev

        return node
    

obj  = Solution()
Solution.reverseList(head)
