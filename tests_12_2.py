from module_12_2 import Runner, Tournament
import unittest


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    def setUp(self):
        self.run1 = Runner('Усэйн', 10)
        self.run2 = Runner('Андрей', 9)
        self.run3 = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results:
            formatted_result = '{' + ', '.join(f'{place}: {runner}' for place, runner in result.items()) + '}'
            print(formatted_result)

    def test_tournament_usain_nick(self):
        tournament = Tournament(90, self.run1, self.run3)
        result1 = tournament.start()
        self.all_results.append(result1)
        self.assertTrue(result1[max(result1.keys())] == 'Ник')

    def test_tournament_andrey_nick(self):
        tournament = Tournament(90, self.run2, self.run3)
        results2 = tournament.start()
        self.all_results.append(results2)
        self.assertTrue(results2[max(results2.keys())] == 'Ник')

    def test_tournament_usain_andrey_nick(self):
        tournament = Tournament(90, self.run1, self.run2, self.run3)
        results2 = tournament.start()
        self.all_results.append(results2)
        self.assertTrue(results2[max(results2.keys())] == 'Ник')


