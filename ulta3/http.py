import asyncio
import os
import time
from concurrent.futures import ThreadPoolExecutor
import requests


def fetch(url: str) -> dict[str, str]:
    # raise NotImplementedError("Not yet implemented Worker")
    started_at = time.monotonic()
    try:
        response = requests.get(url)
    except requests.exceptions.RequestException as e:
        return {"status_code": 500, "time": 0}
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
    return total_time


def run(url: str, requests: int, concurrency: int) -> None:
    results = []
    total = asyncio.run(distribute_work(url, requests, concurrency, results))
    return (total, results)
