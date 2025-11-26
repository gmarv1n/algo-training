from typing import Optional
from list_node import ListNode

# https://leetcode.com/problems/middle-of-the-linked-list/description/?envType=problem-list-v2&envId=linked-list

# Middle of the Linked List
# Given the head of a singly linked list, return the middle node of the linked list.
# If there are two middle nodes, return the second middle node.

# Example 1:
# Input: head = [1,2,3,4,5]
# Output: [3,4,5]
# Explanation: The middle node of the list is node 3.

# Example 2:
# Input: head = [1,2,3,4,5,6]
# Output: [4,5,6]
# Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
 
# Constraints:
# The number of nodes in the list is in the range [1, 100].
# 1 <= Node.val <= 100

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head

        while fast.next:
            # odd iter 1 with
            # 1 2 3 4 5
            # f 
            # s
            # быстрый = некст фаста = 2
            # если у фаста есть некст, то фаст.некст = фаст.некст = 3
            # выход из цикла тк нет фаст.некст и слоу = некст от слоу = 2
            fast = fast.next

            if fast.next:
                fast = fast.next

            slow = slow.next

            # odd iter 2
            # 1 2 3 4 5
            #   s f
            # быстрый = некст фаста = 4
            # если у фаста есть некст, то фаст.некст = фаст.некст = 5
            # слоу = некст от слоу = 3
            # слоу = 3 = middle

            # even iter 1
            # 1 2 3 4
            # f
            # s
            # быстрый = некст фаста = 2
            # если у фаста есть некст, то фаст.некст = фаст.некст = 3
            # слоу = некст от слоу = 2

            # even iter 2
            # 1 2 3 4
            #   s f
            # быстрый = некст фаста = 4
            # если у фаста есть некст, то фаст.некст = фаст.некст = 4
            # слоу = некст от слоу = 3
            # выход из цикла тк нет фаст.некст и слоу = 3 = middle

        return slow
    
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

next = Solution().middleNode(head)

while next:
    print(f"Node {next.val}")
    next = next.next