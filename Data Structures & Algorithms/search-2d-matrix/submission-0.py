class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix)
        while(left<right):
            
            mid = (left+right)//2
            print(left,mid,right)

            if matrix[mid][0]<=target:
                left = mid+1
            else:
                right = mid
        
        targetRow = left-1

        if matrix[targetRow][-1] < target:
            return False


        left = 0
        right = len(matrix[targetRow])
        while(left<right):
            
            mid = (left+right)//2

            if matrix[targetRow][mid]<=target:
                left = mid+1
            else: 
                right = mid
            
        
        return True if matrix[targetRow][left-1] == target else False


        