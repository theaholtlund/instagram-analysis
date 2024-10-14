# Import required libraries
import subprocess
from pathlib import Path
import variables

# Define path to folder where analysis scripts are located
scripts_dir = Path(__file__).resolve().parent / variables.SCRIPTS_DIR

# Function to run a script
def run_script(script_name):
    script_path = scripts_dir / script_name
    if not script_path.exists():
        print(f"Script {script_name} not found.")
        return
    try:
        result = subprocess.run(["python3", script_path], check=True, capture_output=True, text=True)
        print(f"Successfully ran {script_name}:\n{result.stdout}{'=' * 40}\n")
    except subprocess.CalledProcessError as e:
        print(f"There was an error running {script_name}:\n{e.stderr}{'=' * 40}\n")

# Main function to coordinate execution of the script
def main():
    # List all Python files in the analysis script directory
    scripts_to_run = [script.name for script in scripts_dir.glob("*.py")]

    # Run each script in the analysis script directory
    for script in scripts_to_run:
        print(f"Running {script}...")
        run_script(script)

if __name__ == "__main__":
    main()
