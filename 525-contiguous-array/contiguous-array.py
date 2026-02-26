class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count = {}
        maxlen = 0
        total = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                total -= 1
            else:
                total += 1

            if total == 0:
                maxlen = max(maxlen, i + 1)

            if total not in count:
                count[total] = i
            else:
                maxlen = max(maxlen, i - count[total])

        return maxlen