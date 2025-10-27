class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)
        # 90 degrees = transpose and row reverse
        # 0, 90, 180, 270 check for each rotation
        for i in range(4):
            if mat == target:
                return True
            for i in range(n):
                for j in range(i + 1, n):
                    mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
            
            for i in range(n):
                for j in range(n // 2):
                    mat[i][j], mat[i][n - j - 1] = mat[i][n - j - 1], mat[i][j]
        
        return mat == target