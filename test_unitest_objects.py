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
