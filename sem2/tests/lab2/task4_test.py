import unittest
from unittest.mock import patch, AsyncMock
import time
import asyncio

from sem2.src.lab2.task4 import sync_requests, async_requests

class TestAPIRequests(unittest.TestCase):

    @patch('requests.get')
    def test_sync_requests(self, mock_get):
        mock_response = AsyncMock()
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        start_time = time.time()
        sync_requests([
            "https://httpstat.us/200?sleep=3000",
            "https://httpstat.us/200?sleep=1000",
            "https://httpstat.us/200?sleep=2000"
        ])
        end_time = time.time()

        self.assertEqual(mock_get.call_count, 3)

        self.assertLess(end_time - start_time, 15, "Слишком долгое время работы синхронных запросов")

    @patch('aiohttp.ClientSession.get')
    def test_async_requests(self, mock_get):
        mock_response = AsyncMock()
        mock_response.status = 200
        mock_get.return_value.__aenter__.return_value = mock_response

        start_time = time.time()
        asyncio.run(async_requests([
            "https://httpstat.us/200?sleep=3000",
            "https://httpstat.us/200?sleep=1000",
            "https://httpstat.us/200?sleep=2000"
        ]))
        end_time = time.time()

        self.assertEqual(mock_get.call_count, 3)

        self.assertLess(end_time - start_time, 10, "Слишком долгое время работы асинхронных запросов")

    @patch('requests.get')
    @patch('aiohttp.ClientSession.get')
    def test_comparison_sync_vs_async(self, mock_async_get, mock_sync_get):
        mock_sync_response = AsyncMock()
        mock_sync_response.status_code = 200
        mock_sync_get.return_value = mock_sync_response

        mock_async_response = AsyncMock()
        mock_async_response.status = 200
        mock_async_get.return_value.__aenter__.return_value = mock_async_response

        sync_requests([
            "https://httpstat.us/200?sleep=3000",
            "https://httpstat.us/200?sleep=1000",
            "https://httpstat.us/200?sleep=2000"
        ])
        asyncio.run(async_requests([
            "https://httpstat.us/200?sleep=3000",
            "https://httpstat.us/200?sleep=1000",
            "https://httpstat.us/200?sleep=2000"
        ]))

        self.assertEqual(mock_sync_get.call_count, 3)
        self.assertEqual(mock_async_get.call_count, 3)


if __name__ == "__main__":
    unittest.main()
