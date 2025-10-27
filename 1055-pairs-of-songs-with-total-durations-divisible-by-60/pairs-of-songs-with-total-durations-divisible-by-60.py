class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        ans = 0
        count = [0] * 60

        for t in time:
            rem = t % 60
            complement = (60 - rem) % 60
            ans += count[complement]
            count[rem] += 1
        
        return ans