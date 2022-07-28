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


# Name                      Stmts   Miss  Cover
# ---------------------------------------------
# class_loto.py                44     13    70%
# test_pytest_objects.py       24      0   100%
# test_unitest_objects.py      25      0   100%
# ---------------------------------------------
# TOTAL                        93     13    86%

