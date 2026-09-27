class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)
        n=len(matrix[0])
        for i in range(m):
            if i==0 and target<=matrix[i][n-1]:
                return self.find(target,matrix[i]);
            elif i==m-1 and target<=matrix[i][n-1]:
                return self.find(target,matrix[i])
            else:
                cur=matrix[i][n-1]
                prev=matrix[i-1][n-1]
                if target<=cur and target>prev:
                    return self.find(target,matrix[i])
        return False
    def find(self,target,matrix):
        lb=0
        ub=len(matrix)-1
        while lb<=ub:
            mid=(lb+ub)//2
            if matrix[mid]==target:
                return True
            elif target>matrix[mid]:
                lb=mid+1
            else:
                ub=mid-1
        return False
