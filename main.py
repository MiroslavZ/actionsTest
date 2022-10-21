import os

from github import Github
from dotenv import load_dotenv

load_dotenv()
g = Github(os.getenv("TOKEN"))

#HAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHA
for c in g.get_user().get_repo("actionsTest").get_commits():
    print(c)
