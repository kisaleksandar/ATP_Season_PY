from abc import ABC, abstractmethod


class Tournament(ABC):
    def __init__(self, tourName, tourType, tourSurface, numOfSets):
        self._tourName = tourName
        self._tourType = tourType
        self._tourSurface = tourSurface
        self._playable = False
        self._numOfSets = numOfSets

    @abstractmethod
    def play(self):
        pass
