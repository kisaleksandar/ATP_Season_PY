from Tournament import *
from Match import *
from Player import Player
from typing import List, Optional
import random


class SeasonTournament(Tournament):
    def __init__(self, tourName, tourType, tourSurface, numOfSets, championship):
        super().__init__(tourName, tourType, tourSurface, numOfSets)
        self._roundOf16: List[Player] = []
        self._roundOf8: List[Player] = []
        self._semiFinal: List[Player] = []
        self._final: List[Player] = []
        self._losersOf16: List[Player] = []
        self._losersOf8: List[Player] = []
        self._losersOfSemiFinal: List[Player] = []
        self._viceChampion: Optional[Player] = None
        self._champion: Optional[Player] = None
        self._championship = championship

    def play(self):
        self.ResetOfRoundLists()

        self._roundOf16 = self._championship.getPlayersForTournament()
        random.shuffle(self._roundOf16)

        self.playRound(self._roundOf16, self._roundOf8, self._losersOf16, "RoundOf16")
        self.playRound(self._roundOf8, self._semiFinal, self._losersOf8, "RoundOf8")
        self.playRound(self._semiFinal, self._final, self._losersOfSemiFinal, "SemiFinal")

        match = Match(self._final[0], self._final[1], self._tourSurface, self._numOfSets)
        winner, loser = match.playMatch()
        self._viceChampion = loser
        self._champion = winner

        self.PointsPerPhase()
        match.printMatchResult("FINAL")

    def playRound(self, current_round, next_round, losers, phase_name):
        for i in range(0, len(current_round), 2):
            match = Match(current_round[i], current_round[i + 1], self._tourSurface, self._numOfSets)
            winner, loser = match.playMatch()
            match.printMatchResult(phase_name)
            next_round.append(winner)
            losers.append(loser)

    def PointsPerPhase(self):
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

        for loser in self._losersOf16:
            self._championship.updateAtpRanks(loser, predict_dict["RoundOf16"])
        for loser in self._losersOf8:
            self._championship.updateAtpRanks(loser, predict_dict["RoundOf8"])
        for loser in self._losersOfSemiFinal:
            self._championship.updateAtpRanks(loser, predict_dict["SemiFinal"])

        self._championship.updateAtpRanks(self._viceChampion, predict_dict["vice_champion"])
        self._championship.updateAtpRanks(self._champion, predict_dict["champion"])

    def ResetOfRoundLists(self):
        self._roundOf16 = []
        self._roundOf8 = []
        self._semiFinal = []
        self._final = []
        self._losersOf16 = []
        self._losersOf8 = []
        self._losersOfSemiFinal = []
        self._viceChampion = None
        self._champion = None
