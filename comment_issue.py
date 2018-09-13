"""
this script leaves a comment in an existing issue
- this requires the repo owner's id, the repo id, and the issue number
"""


import asyncio
import os
import aiohttp
from gidgethub.aiohttp import GitHubAPI


with open('next_comment.txt', 'r') as cmnt:
    text_object = cmnt.read()


async def main():
    async with aiohttp.ClientSession() as session:
        gh = GitHubAPI(session, "geokai", oauth_token=os.getenv("GH_AUTH"))
        await gh.post('/repos/mariatta/strange-relationship/issues/128/comments',
              data={
                  'title': 'My next comment',
                  'body': text_object,
              })


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
