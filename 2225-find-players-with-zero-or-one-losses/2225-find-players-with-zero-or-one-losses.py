from collections import defaultdict

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        match_count = defaultdict(int)
        losses = defaultdict(int)
        
        for winner, loser in matches:
            match_count[winner] += 1
            losses[loser] += 1
            
        no_losses = []
        one_loss = []
        
        for player in match_count: 
            if losses[player] == 0:
                no_losses.append(player)

        for player, loss_count in losses.items():
            if loss_count == 1:
                one_loss.append(player)
                
        return [sorted(no_losses), sorted(one_loss)]