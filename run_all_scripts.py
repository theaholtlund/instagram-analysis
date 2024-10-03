# Import required libraries
import os
import subprocess

# Define path to the folder where analysis scripts are located
scripts_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'analysis_scripts')

# Functionality to run all scripts in analysis directory
def run_script(script_name):
    script_path = os.path.join(scripts_dir, script_name)
    try:
        # Run the script and wait for process to complete
        result = subprocess.run(["python3", script_path], check=True, capture_output=True, text=True)
        print(f"Successfully ran {script_name}:\n{result.stdout}")
    except subprocess.CalledProcessError as e:
        print(f"Error running {script_name}:\n{e.stderr}")

# Main function to coordinate execution of the script
def main():
    # List all Python files in the analysis_scripts directory
    scripts_to_run = os.listdir(scripts_dir)

    if not scripts_to_run:
        print("No scripts found in the analysis_scripts directory.")
        return

    # Run each script
    for script in scripts_to_run:
        print(f"Running {script}...")
        run_script(script)
        print(f"Finished running {script}\n{'=' * 40}\n")

if __name__ == "__main__":
    main()
