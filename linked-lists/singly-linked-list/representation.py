class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        

    def initial_creation(self, nums: list[int]):
        if not nums:
            head = None
        elif len(nums) == 1:
            head = ListNode(nums[0])
        else:
            node = ListNode(nums[0])
            head = node
            for nxt in nums[1:]:
                next_node = ListNode(nxt)
                node.next = next_node
                node = next_node
    
        return head
    

    def append(self, node: int) -> None:
        tail = self
        while tail.next:
            tail = tail.next
        tail.next = node


    def view_tail(self) -> int:
        tail = self
        while tail.next:
            tail = tail.next
            
        return tail.val


linkked_list = ListNode()
head = linkked_list.initial_creation(nums=list(map(int, input().split())))

