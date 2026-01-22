from collections import defaultdict
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        loss = defaultdict(int)
        players = set()
        
        answer = [[],[]]
        for winner, loser in matches:
            players.add(winner)
            players.add(loser)
            loss[loser] += 1
        
        for player in players:
            if loss[player] == 0:
                answer[0].append(player)
            
            if loss[player] == 1:
                answer[1].append(player)
        
        answer[0].sort()
        answer[1].sort()
        
        return answer
                
