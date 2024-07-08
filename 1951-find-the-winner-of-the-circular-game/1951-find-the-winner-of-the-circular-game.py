class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        # step 1. start at friend 1.
        # count 2 friends clockwise, which are firends 1 and 2.
        losers = []
        # friend 2 leaves the circle, Next start is friend 3.
        # losers.append(k)
        players = [i for i in range(1, n + 1) if i not in losers]
        while len(players) != 1 :
            # print('\n')
            # print(players)
            index = (k % len(players)) - 1
            # print(k, len(players), index)
            if index < 0 : index += len(players)
            losers.append(players[index])
            players.pop(index)
            # print(players)
            # print(losers)

            players = players[index:] + players[:index]
            # print(players)
         
        return players[0]