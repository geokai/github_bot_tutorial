"""
a github bot that,
greets people who create issues in my project,
says thanks when a pull request has been closed,
applies a label to issues or pull requests,
gives a thumbs up reaction to comments I make
"""

import asyncio
import os
import aiohttp
from gidgethub.aiohttp import GitHubAPI


async def main():
    async with aiohttp.ClientSession() as session:
        gh = GitHubAPI(session, "geokai", oauth_token=os.getenv("GH_AUTH"))
        await gh.post('/repos/mariatta/strange-relationship/issues',
              data={
                  'title': 'A new issue to test',
                  'body': 'geokai says, I\'m almost a bot',
              })


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
