# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node = head
        length = 0
        while node:
            node = node.next
            length += 1

        new_node = head
        prev = head
        index = 0
        while new_node:
            if length - n == index:
                if index == 0:
                    return head.next
                else:
                    prev.next = new_node.next
                    break
            prev = new_node
            new_node = prev.next
            index += 1
        return head


list_node = [1]
head = ListNode(list_node[0])
node = head
for v in list_node[1:]:
    node.next = ListNode(v)
    node = node.next

solution = Solution()
print(solution.removeNthFromEnd(head, 1))
head = solution.removeNthFromEnd(head, 1)
while head:
    print(head.val, end=' ')
    head = head.next
