import unittest

from wchain import WChain


class WChainTest(unittest.TestCase):

    def test_chain1(self):
        w = WChain("test_wchain1.in")
        self.assertEqual(6, w.count_of_chains())

    def test_chain2(self):
        w = WChain("test_wchain2.in")
        self.assertEqual(3, w.count_of_chains())

    def test_chain3(self):
        w = WChain("test_wchain3.in")
        self.assertEqual(1, w.count_of_chains())

    def test_chain4(self):
        w = WChain("test_wchain4.in")
        self.assertEqual(4, w.count_of_chains())

    def test_chain5(self):
        w = WChain("test_wchain5.in")
        self.assertEqual(3, w.count_of_chains())

    def test_chain6(self):
        w = WChain("test_wchain6.in")
        self.assertEqual(5, w.count_of_chains())

    def test_chain7(self):
        w = WChain("test_wchain7.in")
        self.assertEqual(4, w.count_of_chains())


if __name__ == '__main__':
    unittest.main()
