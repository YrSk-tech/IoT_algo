import unittest
from main import rabina_karpa_algo


class RabinaKarpaTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(rabina_karpa_algo("tre", "gheytregb", 1001), ['Pattern "tre" found at index 4-6'])

    def test2(self):
        self.assertEqual(rabina_karpa_algo("56", "6375477563732356", 1001), ['Pattern "56" found at index 7-8',
                                                                           'Pattern "56" found at index 14-15'])

    def test3(self):
        self.assertEqual(rabina_karpa_algo("8", "shdgsjdsusdd", 10111101111011110111101111011110111), 'No patterns in text found')

    def test4(self):
        self.assertEqual(rabina_karpa_algo("z", "zzzzzzz", 105), ['Pattern "z" found at index 0',
                                                                'Pattern "z" found at index 1',
                                                                'Pattern "z" found at index 2',
                                                                'Pattern "z" found at index 3',
                                                                'Pattern "z" found at index 4',
                                                                'Pattern "z" found at index 5',
                                                                'Pattern "z" found at index 6'])


if __name__ == '__main__':
    unittest.main()
