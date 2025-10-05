class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        positions = {}
        ans = []
        for i in range(len(nums)):
            if nums[i] not in positions:
                positions[nums[i]] = []
            positions[nums[i]].append(i)
        
        for query in queries:
            if query <= len(positions.get(x, [])):
                ans.append(positions[x][query - 1])
            else:
                ans.append(-1)
        
        return ans