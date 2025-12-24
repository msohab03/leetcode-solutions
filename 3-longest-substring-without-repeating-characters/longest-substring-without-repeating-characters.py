from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = defaultdict(int)

        left = 0
        ans = 0

        for right in range(len(s)):
            count[s[right]] += 1

            while count[s[right]] > 1:
                count[s[left]] -= 1
                
                left += 1
                
                if count[s[left]] == 0:
                    del count[s[left]]
            
            ans = max(ans, right - left + 1)
        
        return ans
            
