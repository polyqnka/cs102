import unittest
from sem2.src.lab2.task8 import run_threads

class TestRaceConditionFixed(unittest.TestCase):
    def test_no_race_condition_with_lock(self):
        for _ in range(3):  # Запускаем несколько раз для уверенности
            result = run_threads()
            self.assertEqual(result, 1_000_000, "Счётчик должен быть равен 1_000_000 при использовании Lock")

if __name__ == "__main__":
    unittest.main()
