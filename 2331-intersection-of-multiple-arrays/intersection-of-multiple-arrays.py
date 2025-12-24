from collections import defaultdict
class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        count = defaultdict(int)
        ans = []
        for arr in nums:
            for x in arr:
                count[x] += 1

                if count[x] == len(nums):
                    ans.append(x)
        
        return sorted(ans)