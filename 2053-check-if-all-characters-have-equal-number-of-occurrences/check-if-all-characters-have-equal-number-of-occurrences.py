from collections import defaultdict
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        count = defaultdict(int)
        
        for i in range(len(s)):
            count[s[i]] += 1
        
        first = count[s[0]]
        for value in count.values():
            if value != first:
                return False
        
        return True
                