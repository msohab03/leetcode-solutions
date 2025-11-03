class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        valid_splits = 0
        prefix = [nums[0]]
        n = len(nums)
        for i in range(1, n):
            prefix.append(nums[i] + prefix[i - 1])
        
        for i in range(len(prefix)):
            if 0 <= i < n - 1:
                if prefix[i] >= prefix[n-1] - prefix[i]:
                    valid_splits += 1

        return valid_splits