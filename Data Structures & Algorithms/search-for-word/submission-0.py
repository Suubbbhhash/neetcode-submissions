class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m=len(board)
        n=len(board[0])
        w=len(word)
        if m==1 and n==1:
            return board[0][0]==word
        def backtrack(pos,index):
            i,j=pos
            if index==w:
                return True
            if board[i][j]!=word[index]:
                return False
            temp=board[i][j]
            board[i][j]="#"
            for i_ind,j_ind in [(1,0),(0,1),(-1,0),(0,-1)]:
                a,b=i_ind+i,j_ind+j
                if 0<=a<m and 0<=b<n:
                    if backtrack((a,b),index+1):
                        return True
            board[i][j]=temp
            return False
        for i in range(m):
            for j in range(n):
                if backtrack((i,j),0):
                    return True
        return False