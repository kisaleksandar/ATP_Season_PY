import sys
import os
import pytest

# Dodaje root folder u sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.Match import Match
from src.Player import Player

@pytest.fixture
def p1():
    return Player("Nole", "mentality", "hard", 3, 4750, False)

@pytest.fixture
def p2():
    return Player("Rafael", "forehand", "clay", 11, 2000, False)

@pytest.fixture
def m():
    p1 = Player("Nole", "mentality", "hard", 3, 4750, False)
    p2 = Player("Rafael", "forehand", "clay", 11, 2000, False)
    return Match(p1, p2, "hard", 2)

def test_init():
    p1 = Player("Nole", "mentality", "hard", 3, 4750, False)
    p2 = Player("Rafael", "forehand", "clay", 11, 2000, False)
    match = Match(p1, p2, "hard", 2)
    assert match.pl1 is p1
    assert match.pl2 is p2
    assert match._surface == "hard"
    assert match._winsetnum is 2
    assert isinstance(match._winsetnum, int)
    assert isinstance(match._surface, str)
    assert isinstance(match._player1, Player)
    assert isinstance(match._player2, Player)



def test_chance_event(monkeypatch, p1, p2, m):

    monkeypatch.setattr(m._rng, "randint", lambda a,b : 1)
    assert m._chanceEvent(10) is True

def test_matchwinnerloser(m, p1, p2):
    m._p1sets = 7
    m._p2sets = 6
    assert m.matchWinnerLoser() == (p1,p2)

def test_printmresult(m, capsys):
    m.printMatchResult("FINAL")
    captured = capsys.readouterr().out
    assert "FINAL" in captured












