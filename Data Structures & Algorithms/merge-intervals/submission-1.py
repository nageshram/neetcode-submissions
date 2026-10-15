class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res=[]
        intervals.sort(key=lambda x:x[0])

        for i in range(len(intervals)):
            curr = intervals[i]
            if len(res)==0 and i==0:
                res.append(curr)
            elif curr[0] <= res[-1][1]:
                a = min(curr[0], res[-1][0])
                b= max( curr[1], res[-1][1])
                res.pop()
                res.append([a,b])
            else:
                res.append(curr)
        
        return res





            

        