# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # finding the middle of list :
        if not head:
            return None
        slow= fast = head

        while fast and fast.next:
            slow = slow.next
            fast= fast.next.next
        
        # slow point the middle so its next is the second half
        cur = slow.next
        slow.next= None
        # reverse the second half
        prev= None
        while cur:
            temp = cur.next
            cur.next=prev
            prev = cur # prev hold the head 
            cur = temp
        
        # merge the two half's
        first = head 
        second = prev    
        while first and second:
            temp= first.next
            temp1 = second.next
            first.next=second
            second.next=temp
            first = temp
            second= temp1
            
        #return head




        

        
        