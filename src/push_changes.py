import subprocess
import time
import os


def commit_and_push(commit_message):
    commands = [
        "git add .",
        "git commit -m \"" + commit_message + "\"",
        "git push"
    ]

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