import random
import time

from add_content import addContent
from push_changes import commit_and_push

max_commits = 10
min_commits = 2


commit_messages = [
    "feat: Add user authentication module",
    "fix: Resolve issue with form validation",
    "refactor: Simplify database schema",
    "docs: Update README with installation instructions",
    "style: Format code according to PEP 8 guidelines",
    "test: Add unit tests for user registration",
    "chore: Update dependencies to latest versions",
    "perf: Optimize database queries for faster retrieval",
    "ci: Configure continuous integration for automated testing",
    "revert: Revert previous commit 'fix: Issue #123'",
    "feat(core): Implement JWT authentication",
    "fix(ui): Correct button alignment in header",
    "docs(api): Add API documentation for endpoints",
    "test(e2e): Write end-to-end tests for user login",
    "refactor(auth): Extract authentication logic into separate module",
    "chore(deps): Update npm packages to resolve security vulnerabilities",
    "style(css): Improve code formatting in stylesheets",
    "perf(api): Optimize API response time by caching results",
    "fix: Typo in error message",
    "chore: Cleanup unused assets"
]

commit_count = random.randrange(min_commits, max_commits)
for i in range(commit_count):
    commit_message = random.choice(commit_messages)
    addContent()
    commit_and_push(commit_message)
    time.sleep(2.4)