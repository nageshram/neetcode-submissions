class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[1])

        res =[]
        res.append(intervals[0])

        for i in range(1, len(intervals)):
            if res[-1][1] > intervals[i][0]:
                continue
            else:
                res.append(intervals[i])

        return len(intervals) - len(res)

