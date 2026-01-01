import random


class Player:
    def __init__(self, name, ability, preferedSurface, atpRank, atpPoints, injured):
        self._name = name
        self._ability = ability
        self._preferedSurface = preferedSurface
        self._atpRank = atpRank
        self._atpPoints = atpPoints
        self._injured = injured

    def servePointChance(self, opponent, surface):
        probability = 50
        if self._preferedSurface == surface:
            probability += 5
        if opponent._preferedSurface == surface:
            probability -= 5

        if self._ability == 'mentality':
            probability += 5
        elif self._ability == 'forehand':
            probability += 10
        elif self._ability == 'serve':
            probability += 15

        if opponent._ability == 'mentality':
            probability -= 10
        elif opponent._ability == 'serve':
            probability += 5
        elif opponent._ability == 'backhand':
            probability -= 8


        if self._atpRank < opponent._atpRank:
            diff = opponent._atpRank - self._atpRank
            probability += diff
        else:
            diff = self._atpRank - opponent._atpRank
            probability -= diff


        return probability

    def checkInjury(self):
        if not self._injured:
            if random.randint(1, 100) == 1:
                self._injured = True
        return self._injured

    def addPoints(self, points):
        self._atpPoints += points

    def updateRank(self, rank):
        self._atpRank = rank

    @property
    def points(self):
        return self._atpPoints

    @property
    def name(self):
        return self._name

    @property
    def rank(self):
        return self._atpRank

    @property
    def getName(self):
        return self._name




    def __str__(self):
        return f"Player: {self._name} \nAtpRank: {self._atpRank} \nAtpPoints: {self._atpPoints} \nInjured: {self._injured} \nPreferedSurface: {self._preferedSurface}"



