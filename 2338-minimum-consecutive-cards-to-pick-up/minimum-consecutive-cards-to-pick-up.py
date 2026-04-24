class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        ans = len(cards) + 1
        seen = defaultdict(list)
        for i in range(len(cards)):
            key = cards[i]

            seen[cards[i]].append(i)
        
        for val in seen:
            arr = seen[val]

            for i in range(len(arr) - 1):
                ans = min(ans, arr[i + 1] - arr[i] + 1)

        if ans == len(cards) + 1:
            return -1
        print(seen)
        return ans