from Tournament import *

class AtpFinals(Tournament):
    def __init__(self, tourName, tourType, tourSurface):
        super().__init__(tourName, tourType, tourSurface)
        self._groupA = []
        self._groupB = []
        self._semiFinal = []
        self._final = []

    def play(self):
        pass