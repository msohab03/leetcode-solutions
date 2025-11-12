class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        res = [-1] * n
        rng = 2 * k + 1
        prefix = [nums[0]]

        for i in range(1, n):
            prefix.append(nums[i] + prefix[i - 1])
        
        for i in range(k, n - k):
            curr = 0
            left = i - k
            right = i + k
            curr = prefix[right] - prefix[left - 1]
            if left == 0:
                curr = prefix[right]
            curr = curr // rng
            res[i] = curr
          
        
        return res
        