import pytest
import asyncio
from io import StringIO
import sys

from sem2.src.lab2.asynhr import delayed_message

@pytest.mark.asyncio
async def test_async_print_message():
    captured_output = StringIO()
    sys.stdout = captured_output

    await delayed_message(2, "Hello")

    assert captured_output.getvalue().strip() == "Hello"

    sys.stdout = sys.__stdout__

@pytest.mark.asyncio
async def test_async_wait_time():
    start_time = asyncio.get_event_loop().time()

    await delayed_message(1, "Test")

    end_time = asyncio.get_event_loop().time()

    assert 0.9 <= end_time - start_time <= 1.1
