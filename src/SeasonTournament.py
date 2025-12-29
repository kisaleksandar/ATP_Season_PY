from Tournament import *
from Match import *
import random


class SeasonTournament(Tournament):
    def __init__(self, tourName, tourType, tourSurface, players, championship):
        super().__init__(tourName, tourType, tourSurface)
        self._roundOf16 = []
        self._roundOf8 = []
        self._semiFinal = []
        self._final = []
        self._championship = championship


    def play(self):
        for player in self._championship._players:
            self._roundOf16.append(player)
        random.shuffle(self._roundOf16)

        self.playRound(self._roundOf16, self._roundOf8, "RoundOf16")
        self.playRound(self._roundOf8, self._semiFinal, "RoundOf8")
        self.playRound(self._semiFinal, self._final, "SemiFinal")

        match = Match(self._final[0], self._final[1], self._tourSurface, self._numofSets)
        winner = match.playMatch()
        match.printMatchResult("FINAL")

        pass

    def playRound(self, current_round, next_round, phase_name):
        for i in range(0, len(current_round), 2):
            match = Match(current_round[i], current_round[i + 1], self._tourSurface, self._numofSets)
            winner = match.playMatch()
            match.printMatchResult(phase_name)
            next_round.append(winner)

    def PointsPerPhase(self, phase, winner):
        predict_dict = {}
        points_dict_grand_slam = {
            "RoundOf16": 180,
            "RoundOf8": 360,
            "SemiFinal": 720,
            "vice_champion": 1200,
            "champion": 2000
        }

        points_dict_masters = {
            "RoundOf16": 100,
            "RoundOf8": 200,
            "SemiFinal": 400,
            "vice_champion": 650,
            "champion": 1000
        }

        if self._tourType == "Grand Slam":
            predict_dict = points_dict_grand_slam
        elif self._tourType == "Masters1000":
            predict_dict = points_dict_masters

        if phase == "RoundOf16":
            self._championship.updateAtpRanks(winner, predict_dict["RoundOf16"])
        elif phase == "RoundOf8":
            self._championship.updateAtpRanks(winner, predict_dict["RoundOf8"])
        elif phase == "SemiFinal":
            self._championship.updateAtpRanks(winner, predict_dict["SemiFinal"])
        elif phase == "FINAL":
            for finalist in self._final:
                if finalist == winner:
                    self._championship.updateAtpRanks(finalist, predict_dict["champion"])
                else:
                    self._championship.updateAtpRanks(finalist, predict_dict["vice_champion"])





