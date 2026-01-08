import sys
import os
import pytest

# Dodaje root folder u sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.Player import Player

@pytest.fixture()
def p1():
    return Player("Nole", "mentality", "hard", 3, 4750, False)

@pytest.fixture()
def p2():
    return Player("Rafael", "forehand", "clay", 11, 2000, False)


def test_player_creation(p1):
    assert p1.name == "Nole"
    assert p1._ability == "mentality"
    assert p1.rank == 3
    assert p1.points == 4750
    assert p1._preferedSurface == "hard"
    assert p1._injured == False

def test_player_add_point(p1):
    p1.addPoints(200)
    assert p1.points == 4950

def test_update_rank(p1, p2):
    p1.updateRank(5)
    p2.updateRank(2)
    assert p1.rank == 5
    assert p2.rank == 2

def test_get_name():
    player = Player("Nole", "mentality", "hard", 3, 4750, False)
    assert player.name == "Nole"

def test_serve_point_chance(p1,p2):

    assert p1.servePointChance(p2, "clay") == 58
    chance = p1.servePointChance(p2, "clay")
    assert isinstance(chance, int)

def test_checkinjury_happens(monkeypatch, p1):
    # nateraj random da uvek vrati 1
    monkeypatch.setattr("random.randint", lambda a,b: 1)

    assert p1.checkInjury() is True

def test_checkinjury_happens_negative(monkeypatch, p2):
    # nateraj random da uvek vrati 1
    monkeypatch.setattr("random.randint", lambda a,b: 2)

    assert p2.checkInjury() is False