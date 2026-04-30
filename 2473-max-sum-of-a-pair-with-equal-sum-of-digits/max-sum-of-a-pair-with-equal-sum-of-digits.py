class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        sumsAndNumbers = defaultdict(list)
        largest = -1

        for num in nums:
            
            digsum = 0
            num = str(num)
            for digit in num:
                digsum += int(digit)

            num = int(num)
            
            sumsAndNumbers[digsum].append(num)

            if len(sumsAndNumbers[digsum]) > 2:
                sumsAndNumbers[digsum] = sorted(sumsAndNumbers[digsum])
                sumsAndNumbers[digsum].remove(sumsAndNumbers[digsum][0])


            if len(sumsAndNumbers[digsum]) >= 2:
                largest = max(largest, sum(sumsAndNumbers[digsum]))
        
       

        return largest