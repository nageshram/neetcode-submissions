from collections import deque
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        dq = deque()

        for char in tokens:
            if char not in ['*','-','+',"/"]:
                dq.append(int(char))
            else:
                b=dq.pop()
                a=dq.pop()
                if char == '+':
                    res=a+b
                elif char == '-':
                    res=a-b
                elif char == '*':
                    res = a*b
                else:
                    res =  abs(a) // abs(b)
                    if (a<0) != (b<0): # if both signs are different it returns True
                        res=-res
                dq.append(res)
        
        return dq[-1]

        