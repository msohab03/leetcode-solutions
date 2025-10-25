class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        # tuples = (i, j, k, l) pairs = we just need the amount of pairs
        # split into a, b and search c, d complement
        ab = {}

        count = 0
        # we take the approach of a + b = -(c + d) we find complement in the two hashmap pairs
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] + nums2[j] in ab:
                    ab[nums1[i] + nums2[j]] += 1
                else:
                    ab[nums1[i] + nums2[j]] = 1
        # search for complement
        for k in range(len(nums3)):
            for l in range(len(nums4)):
                # add number of times its occurred
                if -(nums3[k] + nums4[l]) in ab:
                    count += ab[-(nums3[k] + nums4[l])]
               
        print(ab)
        return count