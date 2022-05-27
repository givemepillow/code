# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        node, head, prev = head, head.next, None
        while node and node.next:
            node1 = node
            node2 = node.next
            node3 = node.next.next
            node1.next = node3
            node2.next = node1
            node = node3
            if prev:
                prev.next = node2
            prev = node1
        return head


list_node = [1, 2, 3, 5, 4, 5, 6, 8, 9, 5, 3, 3, 2]
_head = ListNode(list_node[0])
_node = _head
for v in list_node[1:]:
    _node.next = ListNode(v)
    _node = _node.next

solution = Solution()
n = solution.swapPairs(_head)
while n:
    print(n.val)
    n = n.next
