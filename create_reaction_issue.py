"""
create a reaction for a specific issue number
"""

import asyncio
import os
import aiohttp
from gidgethub.aiohttp import GitHubAPI


async def main():
    async with aiohttp.ClientSession() as session:
        gh = GitHubAPI(session, "geokai", oauth_token=os.getenv("GH_AUTH"))
        await gh.post('/repos/mariatta/strange-relationship/issues/127/reactions',
              data={
                  'content': 'hooray',
              }, accept='application/vnd.github.squirrel-girl-preview+jsom')


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
