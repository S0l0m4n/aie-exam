#!/bin/python3
# Given a list of URLs, fetch them concurrently with a max concurrency limit and
# collect the successful JSON results.
#
# Use a semaphore instead of batching to keep the concurrency pipe full.

import asyncio
import httpx
from typing import Optional, Any

URL_BASE = "https://jsonplaceholder.typicode.com/posts/"
OTHER_URL = "https://docs.python.org/3.10/library/stdtypes.html#text-sequence-type-str"

URLS = [
        URL_BASE + "1",
        OTHER_URL,
        URL_BASE + "2",
        URL_BASE + "3",
        URL_BASE + "4",
]

MAX_CONCURRENT = 3

async def fetch_url(client, url) -> Optional[Any]:
    """
    Args:
        client:     httpx.AsyncClient
        url:        URL to fetch
    """
    try:
        resp = await client.head(url)
        if "json" in resp.headers.get('Content-Type', '').lower():
            # response is a JSON object
            resp = await client.get(url)
            print(f"✅ {url}: {resp.status_code}")
            return resp.json()
        else:
            print(f"❌ {url}: Non-JSON response")
    except httpx.ConnectTimeout:
        print(f"❌ {url}: Failed to connect, server too slow")
    except httpx.HTTPError as e:
        print(f"❌ {url}: Error occured, {e}")

async def fetch_all():
    results = []

    # create the semaphore bouncer
    sem = asyncio.Semaphore(MAX_CONCURRENT)

    async def sem_task(client, url):
        # block with semaphore to ensure only X tasks can run at once
        async with sem:
            return await fetch_url(client, url)

    # use AsyncClient to keep the connection open efficiently
    async with httpx.AsyncClient(timeout=6) as client:
        # create all tasks at once
        # -- they won't run until we gather results, controlled by semaphore
        tasks = [ sem_task(client, url) for url in URLS ]
        results.extend(await asyncio.gather(*tasks))

    for count, r in enumerate(results, start=1):
        if r is not None:
            print(f"{count} - {r}")

if __name__ == "__main__":
    asyncio.run(fetch_all())
