class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        

        #check rows
        for row in board:
            mydict = {}
            for i in row:
                if(i == '.'):
                    continue 

                item = int(i)
                if(item>9 or item<0):
                    return False
                if(item in mydict):
                    return False
                mydict[item] = True


        #check col
        for cols in range(len(board)):
            mydict = {}
            for i in board:
                if(i[cols] == '.'):
                    continue 
                item = int(i[cols])
                if(item>9 or item<0):
                    return False
                if(item in mydict):
                    return False
                mydict[item] = True

        #grid check -> grids 1-9

        seq = [[0,3], [3,6], [6,9]]
        
        for i in seq:
            for j in seq:
                
                mydict = {}
                for a in range(i[0], i[1]):
                    for b in range(j[0], j[1]):
                        if(board[a][b] == '.'):
                            continue
                        if(int(board[a][b])>9 or int(board[a][b])<0):
                            return False
                        if(int(board[a][b]) in mydict):
                            return False
                        mydict[int(board[a][b])] = True

                    


        return True