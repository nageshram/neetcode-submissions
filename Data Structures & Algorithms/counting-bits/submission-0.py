class Solution:
    def countBits(self, n: int) -> List[int]:
        
        def count(num):
            count=0
            while num>0:
                r=num%2
                if r==1:
                    count+=1
                num=num//2
            return count
        counts = []
        for i in range(n+1):
            counts.append(count(i))
        
        return counts
        