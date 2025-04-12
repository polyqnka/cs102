import unittest
from unittest.mock import patch
import asyncio
from sem2.src.lab2.task2 import main  # Импортируем main из src.task2

class TestAsyncioFunctions(unittest.TestCase):

    @patch('builtins.print')
    def test_delayed_message(self, mock_print):
        # Запускаем main() с помощью asyncio.run
        asyncio.run(main())

        # Проверяем, что сообщения были выведены в правильном порядке
        mock_print.assert_any_call("message after 1 second")
        mock_print.assert_any_call("message after 2 seconds")
        mock_print.assert_any_call("message after 3 seconds")

        # Проверяем порядок вызовов
        calls = [call[0][0] for call in mock_print.call_args_list]
        self.assertEqual(calls, [
            "message after 1 second",
            "message after 2 seconds",
            "message after 3 seconds"
        ])

if __name__ == '__main__':
    unittest.main()
