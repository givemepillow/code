# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        elif list1 and not list2:
            return list1
        elif list2 and not list1:
            return list2
        if list1.val < list2.val:
            node = list1
            list1 = list1.next
        else:
            node = list2
            list2 = list2.next
        head = node
        while node:
            if not list1:
                node.next = list2
                break
            elif not list2:
                node.next = list1
                break
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next
        return head
