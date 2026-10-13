class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        i=0
        res=[]
        

        # inerval comes ends before new intervals simpley add it 
        while i<n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i+=1
        
        # if new interval ends times is greater than intervals start time means overlap
        # if merged interval again overlaps  with the  interval we have to run  the loop again to repeatedly merge the overlapping intervals
        while i<n and newInterval[1] >= intervals[i][0]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i+=1
        
        res.append(newInterval)

        while i<n :
            res.append(intervals[i])
            i+=1

        return res

        