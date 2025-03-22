import pytest
import asyncio
from sem2.src.lab1.asynci import first_func, second_func

@pytest.mark.asyncio
async def test_first_function(capfd):
    await first_func()
    captured = capfd.readouterr()
    output = captured.out.split('\n')
    assert output[0] == 'Первый принт из first_function'
    assert output[1] == 'Второй принт из first_function'
    assert output[2] == 'Третий принт из first_function'

@pytest.mark.asyncio
async def test_second_function(capfd):
    await second_func()
    captured = capfd.readouterr()
    output = captured.out.split('\n')
    assert output[0] == 'Первый принт из second_function'
    assert output[1] == 'Второй принт из second_function'
    assert output[2] == 'Третий принт из second_function'
    assert output[3] == 'Четвёртый принт из second_function'

