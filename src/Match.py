import random


class Match:
    def __init__(self, player1, player2, surface, winsetnum):
        self._player1 = player1
        self._player2 = player2
        self._surface = surface
        self._winsetnum = winsetnum
        self._p1sets = 0
        self._p2sets = 0
        self._p1gems = 0
        self._p2gems = 0
        self._p1scoreperset = []
        self._p2scoreperset = []
        self._serve = 0
        self._rng = random.Random()

    def playMatch(self):
        self._p1sets = 0
        self._p2sets = 0
        self._p1gems = 0
        self._p2gems = 0
        self._p1scoreperset = []
        self._p2scoreperset = []

        while self._p1sets < self._winsetnum and self._p2sets < self._winsetnum:
            if self._player1.checkInjury():
                self._p2sets = self._winsetnum
                self._p1sets = 0
                for num in range(self._winsetnum):
                    self._p1scoreperset.append(0)
                    self._p2scoreperset.append(6)
                break
            if self._player2.checkInjury():
                self._p2sets = 0
                self._p1sets = self._winsetnum
                for num in range(self._winsetnum):
                    self._p1scoreperset.append(6)
                    self._p2scoreperset.append(0)
                break
            self._playSet()
        return self.matchWinnerLoser()

    def _playSet(self):
        self._p1gems = 0
        self._p2gems = 0

        while True:
            self._playGame()
            if self._p1gems == 6 and self._p2gems == 6:
                self._playTieBreak()
                break

            if self._p1gems >= 6 or self._p2gems >= 6:
                if self._p1gems - self._p2gems >= 2:
                    self._p1sets += 1
                    self._p1scoreperset.append(self._p1gems)
                    self._p2scoreperset.append(self._p2gems)

                    break
                if self._p2gems - self._p1gems >= 2:
                    self._p2sets += 1
                    self._p2scoreperset.append(self._p2gems)
                    self._p1scoreperset.append(self._p1gems)
                    break

    def _playGame(self):
        p1_points = 0
        p2_points = 0

        if self._serve == 0:
            probability = self._player1.servePointChance(self._player2, self._surface)
            self._serve = 1
        else:
            probability = self._player2.servePointChance(self._player1, self._surface)
            self._serve = 0

        while True:
            win = self._chanceEvent(probability)
            if win:
                p1_points += 1
            else:
                p2_points += 1

            if p1_points >= 4 or p2_points >= 4:
                if p1_points - p2_points >= 2:
                    self._p1gems += 1
                    break
                if p2_points - p1_points >= 2:
                    self._p2gems += 1
                    break

    def _playTieBreak(self):
        p1_points = 0
        p2_points = 0

        while True:
            if self._serve == 0:
                probability = self._player1.servePointChance(self._player2, self._surface)
                self._serve = 1
            else:
                probability = self._player2.servePointChance(self._player1, self._surface)
                self._serve = 0

            win = self._chanceEvent(probability)
            if win:
                p1_points += 1
            else:
                p2_points += 1

            if p1_points >= 7 or p2_points >= 7:
                if p1_points - p2_points >= 2:
                    self._p1gems += 1
                    self._p1sets += 1
                    self._p1scoreperset.append(self._p1gems)
                    self._p2scoreperset.append(self._p2gems)
                    break
                if p2_points - p1_points >= 2:
                    self._p2gems += 1
                    self._p2sets += 1
                    self._p1scoreperset.append(self._p1gems)
                    self._p2scoreperset.append(self._p2gems)
                    break

    def _chanceEvent(self, probability):
        return self._rng.randint(1, 100) <= probability

    def printMatchResult(self, phase):

        print(f"=========={phase}===========")
        print(f"{self._player1.name}", end=" ")
        for gems in self._p1scoreperset:
            print(gems, end=" ")
        print(f"{self._p1sets}", end=" ")

        print(f"{self._player2.name}", end=" ")
        for gems in self._p2scoreperset:
            print(gems, end=" ")
        print(f"{self._p2sets}", end=" ")

    def matchWinnerLoser(self):
        if self._p1sets > self._p2sets:
            return self._player1, self._player2
        else:
            return self._player2, self._player1
