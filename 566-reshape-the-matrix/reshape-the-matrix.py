class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        ans = []
        flatlist = []

        rows, cols = len(mat), len(mat[0])

        for i in range(rows):
            for j in range(cols):    
                flatlist.append(mat[i][j])
        
        if r * c != len(flatlist):
            return mat

        for i in range(0, len(flatlist), c):
            ans.append(flatlist[i: i + c])
        
        return ans

      
