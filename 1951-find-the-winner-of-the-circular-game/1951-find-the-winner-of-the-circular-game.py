class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        losers = []
        players = [i for i in range(1, n + 1) if i not in losers]
        while len(players) != 1 :
            index = (k % len(players)) - 1
            if index < 0 : index += len(players)
            losers.append(players[index])
            players.pop(index)
            players = players[index:] + players[:index]
        return players[0]