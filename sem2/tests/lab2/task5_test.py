import unittest
from unittest.mock import patch
import threading

from sem2.src.lab2.task5 import print_with_delay, run_thread

class TestThreadingExample(unittest.TestCase):

    @patch("builtins.print")
    def test_print_with_delay(self, mock_print):
        thread = threading.Thread(target=print_with_delay)
        thread.start()
        thread.join()

        mock_print.assert_called_with("Это строка, выведенная с задержкой.")

    @patch("builtins.print")
    def test_run_thread(self, mock_print):
        run_thread()

        mock_print.assert_any_call("Это строка, выведенная с задержкой.")
        mock_print.assert_any_call("Поток завершен.")

if __name__ == "__main__":
    unittest.main()
