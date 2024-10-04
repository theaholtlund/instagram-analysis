# Import required libraries
import os
import subprocess

# Define path to folder where analysis scripts are located
scripts_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'analysis_scripts')

# Function to run all scripts in analysis directory
def run_script(script_name):
    script_path = os.path.join(scripts_dir, script_name)
    try:
        result = subprocess.run(["python3", script_path], check=True, capture_output=True, text=True)
        print(f"Successfully ran {script_name}:\n{result.stdout}{'=' * 40}\n")
    except subprocess.CalledProcessError as e:
        print(f"There was an error running {script_name}:\n{e.stderr}{'=' * 40}\n")

# Main function to coordinate execution of the script
def main():
    # List all files in the analysis script directory
    scripts_to_run = os.listdir(scripts_dir)

    # Run each script in the analysis script directory
    for script in scripts_to_run:
        print(f"Running {script}...")
        run_script(script)

if __name__ == "__main__":
    main()
