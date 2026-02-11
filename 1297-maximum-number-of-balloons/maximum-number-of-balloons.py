from collections import defaultdict
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        countchar = defaultdict(int)

        for ch in text:
            countchar[ch] += 1
        
        return min(countchar["b"], countchar["a"], countchar["l"] // 2, countchar["o"] // 2, countchar["n"])
        