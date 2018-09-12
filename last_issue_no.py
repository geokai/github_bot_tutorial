"""
This script retreives the latest issue number created by the user
"""


import asyncio
import os
import aiohttp
from gidgethub.aiohttp import GitHubAPI


async def main():
    async with aiohttp.ClientSession() as session:
        gh = GitHubAPI(session, "geokai", oauth_token=os.getenv("GH_AUTH"))
        issue_list = await gh.getitem(
                '/repos/mariatta/strange-relationship/issues?creator=geokai'
                )
        issue_number = issue_list[0]['number']
        print(issue_number)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
