from Player import Player
from SeasonTournament import SeasonTournament


class Championship:
    def __init__(self):
        self._players = []
        self._tournaments = []

    def updateAtpRanks(self, player, points):

        player.addPoints(points)
        self._players.sort(key=lambda p: p.getPoints(), reverse=True)
        for i, player in enumerate(self._players, start=1):
            player.updateRank(i)

    def recoverPlayers(self):
        for player in self._players:
            player._injured = False

    def loadFiles(self):
        with open(r'D:\ATP_Season_PY\data\players.txt', 'r') as f:
            lines1 = f.readlines()
            for line in lines1:
                line = line.strip()
                line = line.split(',')
                player = Player(line[1], line[2], line[3], int(line[0]), int(line[4]), False)
                self._players.append(player)
        with open('D:\\ATP_Season_PY\\data\\tournaments.txt', 'r') as f:
            lines2 = f.readlines()
            for line in lines2:
                line = line.strip()
                line = line.split(',')
                if line[2] == "Grand Slam":
                    tour = SeasonTournament(line[0], line[2], line[1], 3, self)
                elif line[2] == "Masters1000":
                    tour = SeasonTournament(line[0], line[2], line[1], 2, self)
                self._tournaments.append(tour)

    def getPlayersForTournament(self):
        players = list(self._players)
        return players

    def getTournaments(self):
        return self._tournaments



