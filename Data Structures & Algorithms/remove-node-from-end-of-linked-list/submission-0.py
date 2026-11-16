# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        l=0
        temp=head
        while temp:
            l+=1
            temp=temp.next

        #need to remove
        remove = l-n
        temp= head
        prev=None
        for i in range(0,l):
            if remove == i:
                if prev == None:
                    head = head.next
                else:
                    prev.next=temp.next
            prev=temp
            temp=temp.next
        
        return head


