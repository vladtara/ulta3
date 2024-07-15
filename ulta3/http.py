import asyncio
import os
import time
from concurrent.futures import ThreadPoolExecutor
import requests


def fetch(url: str) -> dict[str, str]:
    # raise NotImplementedError("Not yet implemented Worker")
    started_at = time.monotonic()
    response = requests.get(url)
    requeued_time = time.monotonic() - started_at
    return {"status_code": response.status_code, "time": requeued_time}


async def worker(name: str, queue: asyncio.Queue, results: list) -> None:
    loop = asyncio.get_event_loop()

    while True:
        url = await queue.get()
        if os.environ.get("DEBUG"):
            print(f"{name} - Fetching {url}")
        response = await loop.run_in_executor(None, fetch, url)
        results.append(response)
        queue.task_done()


async def distribute_work(
    url: str, requests: int, concurrency: int, results: list
) -> None:
    queue = asyncio.Queue()

    [queue.put_nowait(url) for _ in range(requests)]
    [
        asyncio.create_task(worker(f"worker-{i}", queue, results))
        for i in range(concurrency)
    ]
    started_at = time.monotonic()
    await queue.join()
    total_time = time.monotonic() - started_at
    print(
        f"{concurrency} workers took {total_time:.2f} seconds to complete {len(results)} requests"
    )


def run(url: str, requests: int, concurrency: int) -> None:
    results = []
    asyncio.run(distribute_work(url, requests, concurrency, results))
    print(results)
