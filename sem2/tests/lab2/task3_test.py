import unittest
from unittest.mock import patch
import asyncio
from sem2.src.lab2.task3 import main

class TestAsyncioFunctions(unittest.TestCase):

    @patch('builtins.print')
    def test_delayed_message(self, mock_print):
        asyncio.run(main())

        mock_print.assert_any_call("message after 1 second")
        mock_print.assert_any_call("message after 2 seconds")
        mock_print.assert_any_call("message after 3 seconds")

        calls = [call[0][0] for call in mock_print.call_args_list]
        self.assertTrue("message after 1 second" in calls[0])
        self.assertTrue("message after 2 seconds" in calls[1])
        self.assertTrue("message after 3 seconds" in calls[2])

if __name__ == '__main__':
    unittest.main()
