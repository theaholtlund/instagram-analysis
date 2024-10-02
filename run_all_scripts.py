# Import required libraries
import os
import subprocess

# Define path to the folder where the analysis scripts are located
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

# Functionality to run all scripts in analysis directory
def run_script(script_name):
    script_path = os.path.join(scripts_dir, script_name)
    # Run the script with python3 and wait for it to complete
    result = subprocess.run(["python3", script_path], check=True, capture_output=True, text=True)
    print(f"Successfully ran {script_name}:\n{result.stdout}")
 

# Main function to coordinate execution of the script
def main():
    for script in scripts_to_run:
        print(f"Running {script}...")
        run_script(script)
        print(f"Finished running {script}\n{'=' * 40}\n")

if __name__ == "__main__":
    main()
