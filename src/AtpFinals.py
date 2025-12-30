from Match import Match
from Tournament import *


class AtpFinals(Tournament):
    def __init__(self, tourName, championship):
        super().__init__(tourName, "AtpFinals", "Hard", 2)
        self._AtpFinalPlayers = []
        self._groupA = []
        self._groupATable = {}
        self._groupB = []
        self._groupBTable = {}
        self._semiFinal = []
        self._final = []
        self._championship = championship

    def play(self):
        self.SetDefaultState()

        self._AtpFinalPlayers = self._championship.getPlayersForTournament()[:8]
        for i, player in enumerate(self._AtpFinalPlayers):
            if i % 2 == 0:
                self._groupA.append(player)
                self._groupATable[player] = 0

            else:
                self._groupB.append(player)
                self._groupBTable[player] = 0

        self.playGroupPhase()

        sorted_groupA = sorted(self._groupATable.items(), key=lambda x: x[1], reverse=True)
        sorted_groupB = sorted(self._groupBTable.items(), key=lambda x: x[1], reverse=True)

        for group in [sorted_groupA, sorted_groupB]:
            for key, value in group[:2]:
                self._semiFinal.append(key)

        self.playSemiFinal()
        self.playFinal()

    def playGroupPhase(self):
        for group in [self._groupA, self._groupB]:
            for i in range(len(group)):
                for j in range(i+1, len(group)):
                    match = Match(group[i], group[j], self._tourSurface, self._numOfSets)
                    winner, loser = match.playMatch()
                    if group == self._groupA:
                        match.printMatchResult("GroupA")
                        self._groupATable[winner] += 1
                    if group == self._groupB:
                        match.printMatchResult("GroupB")
                        self._groupBTable[winner] += 1
                    self._championship.updateAtpRanks(winner, 200)

    def playSemiFinal(self):

        match = Match(self._semiFinal[0], self._semiFinal[3], self._tourSurface, self._numOfSets)
        winner, loser = match.playMatch()
        match.printMatchResult("Semi-Final")
        self._final.append(winner)
        self._championship.updateAtpRanks(winner, 400)

        match = Match(self._semiFinal[1], self._semiFinal[2], self._tourSurface, self._numOfSets)
        winner, loser = match.playMatch()
        match.printMatchResult("Semi-Final")
        self._final.append(winner)
        self._championship.updateAtpRanks(winner, 400)

    def playFinal(self):
        match = Match(self._final[0], self._final[1], self._tourSurface, self._numOfSets)
        winner, loser = match.playMatch()
        match.printMatchResult("Final")
        self._final.append(winner)
        self._championship.updateAtpRanks(winner, 500)

    def SetDefaultState(self):
        self._AtpFinalPlayers = []
        self._groupA = []
        self._groupATable = {}
        self._groupB = []
        self._groupBTable = {}
        self._semiFinal = []
        self._final = []
