# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        node = head
        length = -k
        while node:
            length += 1
            node = node.next
        before = None
        new_head, next_head = self.reverse(head, k, before)
        before = head
        while length >= k:
            _before = next_head
            _, next_head = self.reverse(next_head, k, before)
            before = _before
            length -= k
        return new_head

    def reverse(self, head: Optional[ListNode], k: int, before_head: Optional[ListNode]) -> Optional[ListNode]:
        prev = head
        node = head.next
        i = 1
        while node and i < k:
            next_node = node.next
            node.next = prev
            prev = node
            node = next_node
            i += 1
        if before_head:
            before_head.next = prev
        head.next = node
        return prev, node


list_node = [1,2,3,4,5,6,7,8,9]
_head = ListNode(list_node[0])
_node = _head
for v in list_node[1:]:
    _node.next = ListNode(v)
    _node = _node.next

solution = Solution()
n = solution.reverseKGroup(_head, 4)
while n:
    print(n.val)
    n = n.next
