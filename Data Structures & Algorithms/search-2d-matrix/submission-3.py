class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        low = 0
        high = len(matrix)*len(matrix[0])
        
        while(low<=high):

            t = (low+high)//2
            bucket = t//(len(matrix[0]))
            index = t%(len(matrix[0]))

            if(bucket>=len(matrix)):
                return False

            if(matrix[bucket][index]==target):
                return True

            if(matrix[bucket][index]>target):
                high = t-1

            if(matrix[bucket][index]<target):
                low = t+1


    

        return False