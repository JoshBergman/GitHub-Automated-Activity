import random
import time

from add_content import addContent
from push_changes import commit_and_push

max_commits = 10
min_commits = 2

commit_count = random.randrange(min_commits, max_commits)
for i in range(commit_count):
    addContent()
    commit_and_push()
    time.sleep(4)