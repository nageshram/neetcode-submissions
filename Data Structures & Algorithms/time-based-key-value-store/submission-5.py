class TimeMap:

    def __init__(self):
        self.hmap = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.hmap:
            self.hmap[key].append([timestamp,value])
        else:
            self.hmap[key]=[[timestamp, value]]


    def get(self, key: str, timestamp: int) -> str:
        if key in self.hmap:
            li =self.hmap[key]
            start,end = 0, len(li)-1
            prev_value=""
            while start<=end:
                mid=(start+end)//2
                if li[mid][0]==timestamp:
                    return li[mid][1]
                elif li[mid][0]<timestamp:
                    start = mid+1
                    prev_value=li[mid][1]
                else:
                    end = mid-1
                    
                    
            return prev_value
                        
        return ""

        
