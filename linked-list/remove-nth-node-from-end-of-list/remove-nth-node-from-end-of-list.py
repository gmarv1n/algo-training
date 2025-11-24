from typing import Optional

# Given the head of a linked list, remove the nth node from the end of the list and return its head.
#
# Example 1:
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
#
# Example 2:
# Input: head = [1], n = 1
# Output: []
#
# Example 3:
# Input: head = [1,2], n = 1
# Output: [1]

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummyNode = ListNode(0, head)

        currnetNode = dummyNode

        nodesCount = 1
        while currnetNode.next:
            nodesCount += 1
            currnetNode = currnetNode.next

        # got 6 count
        # need to stop on 5(count) + 1(dummyNode) - 2(n) 
        # on 4th node
        # 4th node = 0 1 2 3

        currnetNode = dummyNode

        # python range(5) will iterate from 0 to 4 
        # rangeNeeded will be 6-2=4, so it will iterate 4 times from 0 to 4 
        rangeNeeded = nodesCount-n
        for i in range(rangeNeeded):
            # rangeNeeded - 1 = 3, so on i = 3 we will iterate 4th time and swap the node 
            if i == rangeNeeded-1:
                currnetNode.next = currnetNode.next.next
            else:
                currnetNode = currnetNode.next
            
        
        return dummyNode.next
    
    def removeNthFromEndTwoPtrs(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummyNode = ListNode(0, head)

        fast = dummyNode
        slow = dummyNode

        # move fast to nth node
        for i in range(n):
            fast = fast.next

        # iter 1: f = from 0 to 1
        # iter 2: f = from 1 to 2

        # 0 1 2 3 4 5
        # s   f 

        # 0 1 2 3 4 5
        #   s   f  

        # 0 1 2 3 4 5
        #     s   f 

        # 0 1 2 3 4 5
        #       s   f
        while fast.next:
            fast = fast.next
            slow = slow.next
            
        slow.next = slow.next.next
        
        return dummyNode.next

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
Solution().removeNthFromEndTwoPtrs(head, 2)
Solution().removeNthFromEndTwoPtrs(head, 2)