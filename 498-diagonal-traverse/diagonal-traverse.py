class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        ans = []
        rows, cols = len(mat), len(mat[0])
        cur_row = cur_col = 0
        # variable to act as placeholder for up and down diagonals : up = i -= 1 and j += 1 down = i += 1 and j -= 1
        goingUp = True
        # until m x n numebrs are in ans
        while len(ans) != rows * cols:
            # adding elements going up
            if goingUp:
                while cur_row >= 0 and cur_col < cols:
                    ans.append(mat[cur_row][cur_col])

                    cur_row -= 1
                    cur_col += 1

                # edge case for out of bounds column
                if cur_col == cols:
                    cur_col -= 1
                    cur_row += 2
                else:
                    cur_row += 1
                
                goingUp = False
            
            else:
                while cur_row < rows and cur_col >= 0:
                    ans.append(mat[cur_row][cur_col])

                    cur_row += 1
                    cur_col -= 1
                
                if cur_row == rows:
                    cur_col += 2
                    cur_row -= 1
                else:
                    cur_col += 1
                
                goingUp = True
        
        return ans
