class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int):
        for l in matrix:
            if target in l :
                return True
                Break
        return False