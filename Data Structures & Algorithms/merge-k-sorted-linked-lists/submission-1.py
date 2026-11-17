# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists)<=0:
            return None
        if len(lists)==1 and lists[0] is None:
            return None
        res=[]
        for li in lists:
            l=li
            while l:
                m=l.next
                l.next=None
                res.append(l)
                l=m
        res.sort(key=lambda x:x.val)
        head=res[0] if len(res)>0 else None
        for i in range(1,len(res)):
            res[i-1].next=res[i]


        return head

        