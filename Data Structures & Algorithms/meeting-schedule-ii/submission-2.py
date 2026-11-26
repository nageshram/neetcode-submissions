"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key= lambda x:x.start)

        min_heap = []

        for interval in intervals:
            if min_heap and min_heap[0] <=interval. start:
                heapq.heappop(min_heap)
            heapq.heappush(min_heap, interval.end)

        # occupy the room if meetings end < new interval.start ( pop previou end and add new end ) 
        # if the new interval is not end at room one append new end time to anotehr room at the end return len (min_heap)
        return len(min_heap)


        

        
        return rooms
        