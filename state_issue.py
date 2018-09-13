"""
this script sets the state of an issue - [open|close]
- uses the PATCH method to set the 'state' value
"""


import asyncio
import os
import aiohttp
from gidgethub.aiohttp import GitHubAPI


async def main():
    async with aiohttp.ClientSession() as session:
        gh = GitHubAPI(session, "geokai", oauth_token=os.getenv("GH_AUTH"))
        await gh.patch('/repos/mariatta/strange-relationship/issues/128',
              data={'state': 'closed'},
              )


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
