# utils/git_utils.py
import subprocess
import os
import shutil

def clone_repo(git_url: str, clone_path: str = "./repo"):
    if os.path.exists(clone_path):
        print(f"Removing existing repo at {clone_path}")
        shutil.rmtree(clone_path)

    print(f"Cloning repo from {git_url} to {clone_path}")
    subprocess.run(["git", "clone", git_url, clone_path], check=True)
