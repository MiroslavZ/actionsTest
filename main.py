import os

from github import Github, ContentFile
from dotenv import load_dotenv
from github.Commit import Commit
from github.PullRequest import PullRequest
from github.Repository import Repository

load_dotenv()
token = os.getenv("TOKEN")
g = Github(token)


def get_and_update_content():
    repo = g.get_user().get_repo("actionsTest")
    sha = repo.get_contents('.env').sha
    content_file = repo.update_file('.env','Updated .env file','testmessage',sha)
    print(repo.get_contents('.env').decoded_content)


if __name__ == '__main__':
    get_content()
