import asyncio
import concurrent.futures


def async_map(f, iterable):
    with concurrent.futures.ThreadPoolExecutor(max_workers=len(iterable)) as executor:
        loop = asyncio.get_event_loop()
        futures = [loop.run_in_executor(executor, f, param) for param in iterable]
        return loop.run_until_complete([r for r in asyncio.gather(*futures)])
