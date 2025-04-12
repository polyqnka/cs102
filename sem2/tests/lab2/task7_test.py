import unittest
from sem2.src.lab2.task7 import increment
import threading

class TestRaceCondition(unittest.TestCase):

    def test_race_condition_occurs(self):
        global counter
        incorrect_results = 0
        runs = 5
        for _ in range(runs):
            counter = 0
            threads = [threading.Thread(target=increment) for _ in range(10)]

            for t in threads:
                t.start()
            for t in threads:
                t.join()

            if counter != 1000000:
                incorrect_results += 1

        self.assertGreater(incorrect_results, 0,
                           "Ожидалась хотя бы одна ошибка из-за гонки данных (результат != 1000000)")

    def test_expected_result(self):
        """Проверка ожидаемого результата при корректной синхронизации (как идея, если использовать Lock)"""
        pass


if __name__ == '__main__':
    unittest.main()
