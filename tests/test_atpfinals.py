import sys
import os
import pytest

from src.Championship import Championship

# Dodaje root folder u sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.AtpFinals import AtpFinals
from src.Championship import *
from src.Player import Player

def test_set_default_state_resets_all():
    championship = Championship()
    tour = AtpFinals(championship)
    tour._groupA = ["dummy"]
    tour._semiFinal = ["dummy"]
    tour.SetDefaultState()
    assert tour._groupA == []
    assert tour._semiFinal == []
    assert tour._groupATable == {}
    assert tour._groupB == []
    assert tour._groupBTable == {}
    assert tour._final == []

@pytest.fixture
def p1():
    return Player("Nole", "mentality", "hard", 3, 4750, False)

@pytest.fixture
def p2():
    return Player("Kole", "mentality", "hard", 2, 4760, False)

@pytest.fixture
def p3():
    return Player("Bole", "mentality", "hard", 1, 4900, False)

@pytest.fixture
def p4():
    return Player("le", "mentality", "grass", 5, 2200, False)

@pytest.fixture
def p5():
    return Player("e", "mentality", "hard", 7, 2100, True)

@pytest.fixture
def p6():
    return Player("ole", "mentality", "hard", 6, 2000, False)

@pytest.fixture
def p7():
    return Player("baba", "mentality", "hard", 8, 1700, True)

@pytest.fixture
def p8():
    return Player("ole", "mentality", "hard", 9, 210, False)

def test_groups_and_semi_final_structure(p1, p2, p3, p4, p5, p6, p7, p8):
    tour = AtpFinals(championship)
    tour._AtpFinalPlayers = [p1, p2, p3, p4, p5, p6, p7, p8]
    tour.playGroupPhase()

    # proveravamo da su svi igrači prisutni u tabeli
    for p in tour._groupA + tour._groupB:
        assert p in tour._groupATable or p in tour._groupBTable

    # broj mečeva po grupi
    expected_matches = len(tour._groupA) * (len(tour._groupA) - 1) // 2
    assert sum(tour._groupATable.values()) <= expected_matches