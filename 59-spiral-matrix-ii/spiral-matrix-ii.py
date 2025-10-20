class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[0] * n for _ in range(n)]

        top, bottom = 0, n - 1
        left, right = 0, n - 1
        val = 1
        while top <= bottom:

            #fill in top row
            for i in range(left, right + 1):
                ans[top][i] = val
                val += 1
            top += 1
            #fill in right col
            for i in range(top, bottom + 1):
                ans[i][right] = val
                val += 1
            right -= 1
            #fill in bottom row
            for i in range(right, left - 1, -1):
                ans[bottom][i] = val
                val += 1
            bottom -= 1
            #fill in left col
            for i in range(bottom, top - 1, -1):
                ans[i][left] = val
                val += 1
            left += 1

        return ans