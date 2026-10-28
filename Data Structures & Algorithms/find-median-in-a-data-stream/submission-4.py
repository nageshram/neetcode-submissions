class MedianFinder:

    def __init__(self):
        self.n = 0
        self.li = []
        

    def addNum(self, num: int) -> None:
        self.li.append(num)
        self.n+=1
        

    def findMedian(self) -> float:
        self.li.sort()
        if (self.n % 2) == 0:
            mid1 = (self.n//2)-1
            mid2 = (self.n//2)
            return float((self.li[mid1]+self.li[mid2])/2)
        else:
            return float(self.li[self.n//2])
        