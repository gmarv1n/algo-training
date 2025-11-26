from typing import Optional
from list_node import ListNode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        next = head
        prev = None
  
        while next:
            # next = 1
            # prev = None
            # 1->2->3->4->5->None
            tmp = next.next # запоминаем некст следующей ноды
            # t = 2
            next.next = prev # делаем некст следующей ноды предыдущей нодой (разворачиваем)
            # 1->None 2->3->4->5->None
            prev = next # предыдущющую ноду делаем слудующей
            # prev = 1
            next = tmp # в слеудющую ноду записываем ту ноду, которая была некс следующей ноды до замены некст.некст
            # next = 2

            # Далее идем так:
            # next = 2
            # prev = 1
            # 1->none 2->3->4->5->None
            # tmp = next.next # запоминаем некст следующей ноды
            # tmp становится 3
            # next.next = prev # делаем некст следующей ноды предыдущей нодой (разворачиваем)
            # None<-1<-2 3->4->5->None
            # в этот момент между 2 и 3 связи нет
            # prev = next # предыдущющую ноду делаем следующей
            # prev становится 2
            # next = tmp # в слеудющую ноду записываем ту ноду, которая была некс следующей ноды до замены некст.некст
            # next становится 3
            # ...
            # next = 5
            # prev = 4
            # None<-1<-2<-3<-4 5->None
            # tmp = next.next # запоминаем некст следующей ноды
            # tmp становится None
            # next.next = prev # делаем некст следующей ноды предыдущей нодой (разворачиваем)
            # None<-1<-2<-3<-4<-5
            # prev = next # предыдущющую ноду делаем слекдующей
            # prev становится 5
            # next = tmp # в слеудющую ноду записываем ту ноду, которая была некс следующей ноды до замены некст.некст
            # next становится None

        return prev

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
res = Solution().reverseList(head)

while res.next:
    print(f"Node {res.val}")