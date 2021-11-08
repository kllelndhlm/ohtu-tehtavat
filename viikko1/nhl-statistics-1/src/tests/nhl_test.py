import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
    )

    def test_flyersit(self):
        tulostus = str(self.statistics.team("Philadelphia Flyers"))
        self.assertEqual(tulostus, "[]")

    def test_sorttaus_oikein(self):
        sorttaus = self.statistics.top_scorers(0)
        self.assertEqual(sorttaus, "Top scorers:\nGretzky EDM 35 + 89 = 124\nLemieux PIT 45 + 54 = 99\nYzerman DET 42 + 56 = 98\nKurri EDM 37 + 53 = 90\nSemenko EDM 4 + 12 = 16")

    def test_name(self):
        pelaajahaku = self.statistics.search("Gretzky") 
        self.assertEqual(pelaajahaku, "Gretzky")

    def test_no_name(self):
        pelaajahaku = self.statistics.search("Juti") 
        self.assertIsNone(self.statistics.search("Juti"))
