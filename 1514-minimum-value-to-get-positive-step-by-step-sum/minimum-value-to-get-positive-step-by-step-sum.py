class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        startval = 1
        while True:
            total = startval
            isValid = True
            for num in nums:
                total += num
                if total < 1:
                    isValid = False
                    break
            if isValid:
                return startval
            else:
                startval += 1
                
        
        
            