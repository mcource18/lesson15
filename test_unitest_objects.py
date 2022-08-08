import copy
import unittest

from class_loto import Card, Player


class TestCard(unittest.TestCase):
    def setUp(self):
        self.card=Card("Alex")

    def test_init(self):
        self.assertEqual(self.card.name, "Alex")
        self.assertEqual(len(self.card.field), 3)
        self.assertEqual(len(self.card.field[0]), 5)

    def test_cross(self):
        self.assertTrue(self.card.cross(self.card.field[0][0]))

    def test_str(self):
        self.assertTrue("Alex"  in str(self.card))

    def test_eq1(self):
        card1=Card("Alex")
        card2 = copy.copy(card1)
        self.assertEqual(card1,card2)

    def test_eq2(self):
        card1 = Card("Alex")
        card2 = Card("Max")
        self.assertNotEqual(card1,card2)


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player("Alex",False)

    def test_init(self):
        self.assertEqual(self.player.name, "Alex")
        self.assertFalse(self.player.is_computer)

    def test_testcard(self):
        player = Player("Alex", True)
        self.assertTrue(player.test(3))

    def test_is_all_cross(self):
        self.assertFalse(self.player.is_all_cross())

        for i in range(0,91):
            self.player.test(i)
        self.assertTrue(self.player.is_all_cross())
    def test_str(self):
        self.assertEqual(str(self.player),"{'name': 'Alex', 'is_computer': False}")

    def test_eq1(self):
        player1 = Player("Alex", False)
        player2 = Player("Alex", True)
        self.assertNotEqual(player1,player2)

    def test_eq2(self):
        player1 = Player("Alex", False)
        player2 = Player("Alex", False)
        self.assertEqual(player1,player2)