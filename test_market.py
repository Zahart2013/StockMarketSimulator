from unittest import TestCase
from source.market import Market
from source.network import AI


class TestMarket(TestCase):
    def test_get_basic(self):
        market = Market()
        self.assertIn("AAPL", market.basic.keys())
        self.assertIn("AMD", market.basic.keys())
        self.assertIn("AMZN", market.basic.keys())
        self.assertIn("INTC", market.basic.keys())
        self.assertIn("MSFT", market.basic.keys())
        self.assertIn("CSCO", market.basic.keys())
        self.assertIn("GPRO", market.basic.keys())
        self.assertIn("NVDA", market.basic.keys())
        self.assertEqual(len(market.basic["AAPL"]), 30)

    def test_add_ais(self):
        market = Market()
        self.assertEqual(len(market.ais), 0)
        ais = [AI(market.basic), AI(market.basic)]
        market.add_ais(ais)
        self.assertEqual(len(market.ais), 2)
        ai = AI(market.basic)
        market.add_ais(ai)
        self.assertEqual(len(market.ais), 3)
        self.assertIn(ai, market.ais)

    def test_calculate(self):
        market = Market()
        market.add_ais([AI(market.basic), AI(market.basic), AI(market.basic)])
        for each in market.ais:
            choice = each.choice(market.basic)
            if len(choice.keys()) > 0:
                for key in market.active_offers.keys():
                    market.active_offers[key].append(choice[key])
        market.calculate()
        for each in market.ais:
            self.assertNotEqual(each.money, 8000)
            self.assertNotEqual(each.stocks, {'AAPL': 0, 'AMD': 0, 'AMZN': 0, "INTC": 0, "MSFT": 0, "CSCO": 0, "GPRO": 0, "NVDA": 0})
