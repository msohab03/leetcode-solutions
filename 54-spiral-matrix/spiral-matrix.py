class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row, col = len(matrix), len(matrix[0])
        # go left = row, col - 1
        #go right = row, col + 1
        #go up = row - 1, col
        #go down = row + 1, col
        ans = []
        top, left = 0, 0
        bottom, right = len(matrix), len(matrix[0])

        while left < right and top < bottom:
            # get i in top row
            for i in range(left, right):
                ans.append(matrix[top][i])
            top += 1
            # get i in right col
            for i in range(top, bottom):
                ans.append(matrix[i][right - 1])
            right -= 1
            if not (left < right and top < bottom):
                break
            # get i in bottom row backwards
            for i in range(right - 1, left - 1, -1):
                ans.append(matrix[bottom - 1][i])
            bottom -= 1
            # get i in left col
            for i in range(bottom - 1, top - 1, -1):
                ans.append(matrix[i][left])
            left += 1
        
        return ans
            