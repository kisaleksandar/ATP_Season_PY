from abc import ABC, abstractmethod


class Tournament(ABC):
    def __init__(self, tourName, tourType, tourSurface, players):
        self._tourName = tourName
        self._tourType = tourType
        self._tourSurface = tourSurface
        self._playable = False
        self._numofSets = 0
        self._players = players

    @abstractmethod
    def play(self):
        pass
