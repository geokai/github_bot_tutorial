"""
this script leaves a comment in an existing issue
- this requires the repo owner's id, the repo id, and the issue number
"""


import asyncio
import os
import aiohttp
from gidgethub.aiohttp import GitHubAPI

 
async def main():
    async with aiohttp.ClientSession() as session:
        gh = GitHubAPI(session, "geokai", oauth_token=os.getenv("GH_AUTH"))
        await gh.post('/repos/mariatta/strange-relationship/issues/127/comments',
              data={
                  'title': 'My first comment',
                  'body': 'I hope I got this comment thing right!',
              })


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
