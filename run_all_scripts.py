# Import required libraries
import os
import subprocess

# Define the path to the folder where the analysis scripts are located
scripts_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'analysis_scripts')

# List of scripts to run
scripts_to_run = [
    "blocked_accounts.py",
    "close_friends.py",
    "content_comments.py",
    "count_comments.py",
    "count_liked_comments.py",
    "count_liked_posts.py",
    "most_liked_posts.py",
    "not_following_back.py"
]
