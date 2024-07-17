import asyncio
import os
import time
from concurrent.futures import ThreadPoolExecutor
import requests


import time
import requests

def fetch(url: str) -> dict[str, str]:
    """
    Fetches the content of a given URL and returns the response status code and the time taken to fetch the content.

    Args:
        url (str): The URL to fetch the content from.

    Returns:
        dict[str, str]: A dictionary containing the response status code and the time taken to fetch the content.

    Raises:
        None

    """
    started_at = time.monotonic()
    try:
        response = requests.get(url)
    except requests.exceptions.RequestException as e:
        return {"status_code": 500, "time": 0}
    requeued_time = time.monotonic() - started_at
    return {"status_code": response.status_code, "time": requeued_time}


async def worker(name: str, queue: asyncio.Queue, results: list) -> None:
    """
    Asynchronous worker function that fetches URLs from a queue and appends the response to a results list.

    Args:
        name (str): The name of the worker.
        queue (asyncio.Queue): The queue containing the URLs to fetch.
        results (list): The list to which the fetched responses will be appended.

    Returns:
        None

    """
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
    """
    Distributes work among multiple workers to send HTTP requests concurrently.

    Args:
        url (str): The URL to send the HTTP requests to.
        requests (int): The number of HTTP requests to send.
        concurrency (int): The number of workers to create for concurrent processing.
        results (list): A list to store the results of the HTTP requests.

    Returns:
        None

    """
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


import asyncio

def run(url: str, requests: int, concurrency: int) -> None:
    """
    Executes HTTP requests to a given URL in parallel using asyncio.

    Args:
        url (str): The URL to send the HTTP requests to.
        requests (int): The number of HTTP requests to send.
        concurrency (int): The maximum number of requests to send concurrently.

    Returns:
        tuple: A tuple containing the total number of requests sent and a list of results.

    """
    results = []
    total = asyncio.run(distribute_work(url, requests, concurrency, results))
    return (total, results)
