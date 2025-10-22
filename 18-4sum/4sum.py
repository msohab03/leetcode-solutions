class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        current = []
        nums.sort()
        def kSum(k, start, target):
            # needs to no larger than 2 in order to do two pointer approach
            if k != 2:
                # non base case
                # we want to leave the last 3 elements / enough to get a quad pair
                for i in range(start, len(nums) - k + 1):
                    # no duplicates
                    if i > start and nums[i] == nums[i - 1]:
                        continue
                    # add to current array
                    current.append(nums[i])
                    # smaller recursion 
                    kSum(k - 1, i + 1, target - nums[i])
                    # remove last from current array
                    current.pop()
                # we dont want the bottom approach to be executed unless we have 2
                return
            
            # start of two pointer approach
            l, r = start, len(nums) - 1
            # while to keep looping until base case
            while l < r:
                if nums[l] + nums[r] > target:
                    r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    ans.append(current + [nums[l], nums[r]])
                    l += 1
                    r -= 1

                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
        
        kSum(4, 0, target)

        return ans


