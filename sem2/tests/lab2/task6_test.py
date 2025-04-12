import unittest
from unittest.mock import patch
import time
from sem2.src.lab2.task6 import run_sequential, run_with_threads


class TestTask6(unittest.TestCase):

    @patch("builtins.print")
    def test_run_sequential_time(self, mock_print):
        start = time.time()
        run_sequential()
        duration = time.time() - start
        self.assertGreaterEqual(duration, 6, "Время выполнения должно быть >= 6 секунд")

    @patch("builtins.print")
    def test_run_with_threads_time(self, mock_print):
        start = time.time()
        run_with_threads()
        duration = time.time() - start
        self.assertLess(duration, 6, "Время выполнения должно быть < 6 секунд")

    @patch("builtins.print")
    def test_parallel_faster_than_sequential(self, mock_print):
        start_seq = time.time()
        run_sequential()
        duration_seq = time.time() - start_seq

        start_threads = time.time()
        run_with_threads()
        duration_threads = time.time() - start_threads

        self.assertLess(duration_threads, duration_seq,
                        "Параллельный запуск должен быть быстрее последовательного")


if __name__ == '__main__':
    unittest.main()
