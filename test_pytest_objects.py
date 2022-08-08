import copy
from class_loto import Card, Player


class TestCard:
    def test_init(self):
        card = Card("Alex")
        assert card.name == "Alex"
        assert len(card.field) == 3
        assert len(card.field[0]) == 5

    def test_cross(self):
        card = Card("Alex")
        assert card.cross(card.field[0][0])

    def test_str(self):
        card=Card("Alex")
        assert "Alex"  in str(card)

    def test_eq1(self):
        card1=Card("Alex")
        card2 = copy.copy(card1)
        assert card1==card2

    def test_eq2(self):
        card1 = Card("Alex")
        card2 = Card("Max")
        assert card1 != card2

class TestPlayer:
    def test_init(self):
        player = Player("Alex",False)
        assert player.name == "Alex"
        assert player.is_computer == False

    def test_testcard(self):
        player = Player("Alex",True)
        assert player.test(3)

    def test_is_all_cross(self):
        player = Player("Alex", True)
        assert not player.is_all_cross()
        for i in range(0,91):
            player.test(i)
        assert player.is_all_cross()

    def test_str(self):
        player = Player("Alex", False)
        assert str(player)=="{'name': 'Alex', 'is_computer': False}"

    def test_eq1(self):
        player1 = Player("Alex", False)
        player2 = Player("Alex", True)
        assert player1!=player2

    def test_eq2(self):
        player1 = Player("Alex", False)
        player2 = Player("Alex", False)
        assert player1==player2


# Name                      Stmts   Miss  Cover
# ---------------------------------------------
# class_loto.py                44     13    70%
# test_pytest_objects.py       24      0   100%
# test_unitest_objects.py      25      0   100%
# ---------------------------------------------
# TOTAL                        93     13    86%

