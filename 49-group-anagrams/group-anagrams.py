class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)

        for st in strs:
            key = "".join(sorted(st))

            ans[key].append(st)
        
        return list(ans.values())