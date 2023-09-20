import random
import subprocess
import time
import os

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

commands = [
    "git add .",
    "git commit -m \"" + random.choice(commit_messages) + "\"",
    "git push"
]

def commit_and_push():
    path = os.path.dirname(os.path.abspath(__file__))
    os.chdir(path)

    for command in commands:    
        time.sleep(1)
        try:
            result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            if result.returncode == 0:
                print(result.stdout)
            else:
                print("Failed To Run Command: \n\n")
                print(result.stderr)
        except Exception as e:
            print(f"Error Running Command: \n\n {e}")