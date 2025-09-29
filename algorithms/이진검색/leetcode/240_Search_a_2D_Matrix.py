class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #target이 현재 메트릭 위치보다 작으면 왼쪽으로 크면 아래로 이동하는 방법. 
        if not matrix:
            return False
        
        row=0
        col=len(matrix[0])-1

        while row<=len(matrix)-1 and 0<=col:
            if matrix[row][col]==target:
                return True
            elif matrix[row][col]>target:
                col-=1
            elif matrix[row][col]<target:
                row+=1
        return False