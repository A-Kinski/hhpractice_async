from time import time
import asyncio

import aiohttp

from fetcher_sync import imgs, base_url

async def fetch_content(url, session):
    async with session.get(url, allow_redirects=True) as response:
        data = await response.read()


async def main():
    async with aiohttp.ClientSession() as session:
        tasks = []
        for img in imgs:
            task = asyncio.create_task(fetch_content(base_url + img, session))
            tasks.append(task)
        
        await asyncio.gather(*tasks)

if __name__ == '__main__':
    t0 = time()
    asyncio.run(main())
    print(time() - t0)
