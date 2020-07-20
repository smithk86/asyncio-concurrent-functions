import asyncio
import random
from functools import partial

import pytest

from asyncio_concurrent_functions import AsyncioConcurrentFunctions


@pytest.mark.asyncio
async def test_concurrent_functions():
    async def _test_function(wait_time):
        await asyncio.sleep(wait_time)
        return wait_time

    funcs = []
    wait_times = [
        0.4,
        0.2,
        0.3,
        0.1,
        0.5
    ]

    for wait_time in wait_times:
        funcs.append(partial(_test_function, wait_time))

    results_1 = list()
    async for result in AsyncioConcurrentFunctions(funcs, workers=5):
        results_1.append(result)
    assert results_1 == [0.1, 0.2, 0.3, 0.4, 0.5]

    results_2 = list()
    async for result in AsyncioConcurrentFunctions(funcs, workers=2):
        results_2.append(result)
    assert results_2 == [0.2, 0.4, 0.3, 0.1, 0.5]
