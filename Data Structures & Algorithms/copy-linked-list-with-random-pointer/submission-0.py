"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        arr = []
        index_map={}
        curr = head
        while curr:
            index_map[curr]= len(arr)
            arr.append([curr, None, None])
            curr=curr.next
        
        for i in range(len(arr)):
            node = arr[i][0]
            #updating the next pointer 
            if node.next is not None:
                arr[i][1] = index_map[node.next]
            if arr[i][0].random is not None:
                arr[i][2] = index_map[node.random]
        
        cloned = [ Node(x =item[0].val) for item in arr]

        # rebuild the cloned one :
        for i in range(len(cloned)):
            next_index = arr[i][1]
            random_index = arr[i][2]

            if next_index is not None:
                cloned[i].next = cloned[next_index]
            if random_index is not None:
                cloned[i].random = cloned[random_index]
        return cloned[0]


        