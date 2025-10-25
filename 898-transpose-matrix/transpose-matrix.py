class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row, col = len(matrix), len(matrix[0])
        transpose_matrix = []

        for i in range(col):
            temp = []
            for j in range(row):
                temp.append(matrix[j][i])
            transpose_matrix.append(temp)
        return transpose_matrix
        