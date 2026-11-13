from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)<=1:
            return False
        stack = deque()
        pairs = { ')':'(', '}':'{', ']':'['}

        for c in s:
            if c in '({[':
                stack.append(c)
            else:
                if not stack or stack[-1] != pairs[c]:
                    return False
                stack.pop() # in case matched pop it 
        return True if not stack else False
            


            


