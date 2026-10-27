import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        li = []
        
        for i in range(len(points)):
            distance = math.sqrt((points[i][0]- 0)**2 + ( points[i][1]-0)**2)
            li.append([distance,points[i]])
        li.sort(key= lambda x: x[0])

        return [li[i][1] for i in range(k)]
    