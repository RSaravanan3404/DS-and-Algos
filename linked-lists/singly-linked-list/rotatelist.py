from representation import ListNode, head


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or k == 0:
            return head
        
        tail = head
        length = 1
        while tail.next:
                tail = tail.next
                length += 1

        tail.next = head
        k %= length

        new_tail_index = length - k - 1
        new_tail = head
        for _ in range(new_tail_index):
            new_tail = new_tail.next

        new_head = new_tail.next
        new_tail.next = None

        return new_head
    

obj  = Solution()
Solution.rotateRight(head, int(input()))