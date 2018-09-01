"""
this script closes an open issue
- uses the PATCH method to send the command
"""


import asyncio
import os
import aiohttp
from gidgethub.aiohttp import GitHubAPI


async def main():
    async with aiohttp.ClientSession() as session:
        gh = GitHubAPI(session, "geokai", oauth_token=os.getenv("GH_AUTH"))
        await gh.patch('/repos/mariatta/strange-relationship/issues/127',
              data={'state': 'closed'},
              )


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
