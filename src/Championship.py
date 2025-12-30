from Player import Player
from Tournament import Tournament


class Championship:
    def __init__(self):
        self._players = []
        self._tournaments = []

    def updateAtpRanks(self, winner, points):
        winner._atpPoints += points
        self._players.sort(key=lambda p: p._atpPoints, reverse=True)
        for i, player in enumerate(self._players, start =1):
            player._atpRank = i



    def recoverPlayers(self):
        for player in self._players:
            player._injured = False

    def loadFiles(self):
        with open('D:\\ATP_Season_PY\\data\\players.txt', 'r') as f:
            lines1 = f.readlines()
            for line in lines1:
                line = line.strip()
                line = line.split(',')
                player = Player(line[0], line[1], line[2], line[3], line[4], False)
                self._players.append(player)
        with open('D:\\ATP_Season_PY\\data\\tournaments.txt', 'r') as f:
            lines2 = f.readlines()
            for line in lines2:
                line = line.strip()
                line = line.split(',')
                tour = Tournament(line[0], line[2], line[1])
                self._tournaments.append(line)

    def getPlayersForTournament(self):
        players = list(self._players)
        return players

