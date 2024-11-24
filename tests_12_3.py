import unittest


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


class RunnerTest(unittest.TestCase):
    is_frozen = False

    def test_walk(self):
       i = Runner("test")
       for _ in range(10):
           i.walk()
       self.assertEqual(i.distance, 50)

    def test_run(self):
        j = Runner("test2")
        for _ in range(10):
            j.run()
        self.assertEqual(j.distance, 100)

    def test_challenge(self):
        ii = Runner("test3")
        jj = Runner("test4")
        for _ in range(10):
            ii.walk()
            jj.run()
        self.assertNotEqual(ii.distance, jj.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def setUp(self):
        self.Usein = Runner("Usein", 10)
        self.Andrey = Runner("Andrey", 9)
        self.Nik = Runner("Nik", 3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            show_result = {}
            for place, runner in result.items():
                show_result[place] = runner.name
            print(show_result)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run_1(self):
        self.tournament = Tournament(90, self.Usein, self.Nik)
        self.all_results = self.tournament.start()
        last_runner_name = self.all_results[max(self.all_results.keys())].name
        self.assertTrue(last_runner_name == "Nik")
        TournamentTest.all_results[1] = self.all_results

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run_2(self):
        self.tournament_2 = Tournament(90, self.Andrey, self.Nik)
        self.all_results = self.tournament_2.start()
        last_runner_name = self.all_results[max(self.all_results.keys())].name
        self.assertTrue(last_runner_name == "Nik")
        TournamentTest.all_results[2] = self.all_results

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run_3(self):
        self.tournament_3 = Tournament(90, self.Usein, self.Andrey, self.Nik)
        self.all_results = self.tournament_3.start()
        last_runner_name = self.all_results[max(self.all_results.keys())].name
        self.assertTrue(last_runner_name == 'Nik')
        TournamentTest.all_results[3] = self.all_results


if __name__ == '__main__':
    unittest.main()