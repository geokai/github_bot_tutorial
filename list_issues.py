"""
This script retreives a listing of issues created by the user
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
        # print(issue_list[0]['number'])
        for i in issue_list:
            print('issue', i['number'])
            print(i)
            print()


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
