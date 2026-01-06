#!/bin/python3
# Given a list of URLs, fetch them concurrently with a max concurrency limit and
# collect the successful JSON results.

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
        if "json" in resp.headers['Content-Type']:
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

    # use AsyncClient to keep the connection open efficiently
    async with httpx.AsyncClient(timeout=6) as client:
        for count, i in enumerate(range(0, len(URLS), MAX_CONCURRENT), start=1):
            batch = URLS[i : i + MAX_CONCURRENT]
            tasks = [ fetch_url(client, url) for url in batch ]
            print(f"Processing batch {count}...")
            # use extend (not append) to keep the list flat
            results.extend(await asyncio.gather(*tasks))

    print(results)

if __name__ == "__main__":
    asyncio.run(fetch_all())
