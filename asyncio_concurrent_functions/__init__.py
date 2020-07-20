import asyncio
import sys

from asyncio_pool import AioPool


__VERSION__ = '1.0'
__DATE__ = '2020-07-20'
__MIN_PYTHON__ = (3, 7)


if sys.version_info < __MIN_PYTHON__:
    sys.exit('python {}.{} or later is required'.format(*__MIN_PYTHON__))



class AsyncioConcurrentFunctions(object):
    def __init__(self, list_of_funcs, workers=10):
        self.list_of_funcs = list_of_funcs
        self.pool = AioPool(workers)
        self.queue = asyncio.Queue()

    async def __aenter__(self):
        return self

    async def __aexit__(self, *exc):
        pass

    async def spawner(self):
        async def _add(func):
            await self.queue.put(await func())

        async with self.pool:
            for func in self.list_of_funcs:
                await self.pool.spawn(_add(func))
        await self.queue.put(StopAsyncIteration)

    async def __aiter__(self):
        task = asyncio.create_task(self.spawner())
        try:
            while True:
                val = await self.queue.get()
                if val is StopAsyncIteration:
                    break
                else:
                    yield val
        finally:
            await task
