from collections import defaultdict
class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        numbers = defaultdict(int)
        answer = -1
        
        for num in nums:
            numbers[num] += 1
        
        for key, value in numbers.items():
            if value == 1:
                answer = max(answer, key)
        
        return answer