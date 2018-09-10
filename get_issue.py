"""
this script retrieves an existing issue by issue number
- the issue number must be aquired beforehand by other means
"""


import asyncio
import os
import aiohttp
from gidgethub.aiohttp import GitHubAPI


async def main():
    async with aiohttp.ClientSession() as session:
        gh = GitHubAPI(session, "geokai", oauth_token=os.getenv("GH_AUTH"))
        item = await gh.getitem('/repos/mariatta/strange-relationship/issues/127')
        print(item)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
