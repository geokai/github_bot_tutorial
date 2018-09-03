"""
A class containing the basic methods for interacting with the github bot api.
"""


import asyncio
import os
import aiohttp
from gidgethub.aiohttp import GitHubAPI

 
 class Gitbot_api(object):
     """Gitbot_api class provides the methods required to interact with
     the github api.
     """

    def __init__(self):
        """initialize an instant of the api bot"""
        pass

    def create_issue(self):
        """method to create an issue"""
        pass

    def comment_issue(self):
        """method to issue a comment to an existing issue"""
        pass

    def close_issue(self):
        """method to close an issu"""
        pass

    def send_reaction_issue(self):
        """method to send a reaction to an existing issue"""

    def get_reaction_issue(self):
        """method to retriev a reaction from an existing issue"""
        pass
