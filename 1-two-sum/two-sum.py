class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsHash = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in numsHash and numsHash[complement] != i:
                return [i, numsHash[complement]]
            
            numsHash[nums[i]] = i
        return []