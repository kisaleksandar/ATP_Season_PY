from Tournament import *

class SeasonTournament(Tournament):
    def __init__(self, tourName, tourType, tourSurface):
        super().__init__(tourName, tourType, tourSurface)
        self._roundOf16 = []
        self._roundOf8 = []
        self._semiFinal = []
        self._final = []

    def play(self):
        pass

