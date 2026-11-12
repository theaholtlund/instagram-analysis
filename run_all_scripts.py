"""Run the Instagram analysis scripts."""

import subprocess
import sys
from pathlib import Path
from instagram_analysis import variables

scripts_dir = Path(__file__).resolve().parent / variables.SCRIPTS_DIR


def run_script(script_name):
    """Run a specific Python script from the analysis_scripts directory."""
    script_path = scripts_dir / script_name
    if not script_path.exists():
        print(f"Error: Script '{script_name}' not found.")
        return

    try:
        result = subprocess.run(
            [sys.executable, script_path], check=True, capture_output=True, text=True
        )
        print(f"Successfully ran '{script_name}':\n{result.stdout}\n{'=' * 40}\n")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error running '{script_name}':\n{e.stderr}\n{'=' * 40}\n")
        return False
    except Exception as e:
        print(
            f"An unexpected error occurred while running '{script_name}': {e}\n{'=' * 40}\n"
        )
        return False


def main():
    """Run all Python scripts in the analysis_scripts directory."""
    scripts_to_run = sorted(script.name for script in scripts_dir.glob("*.py"))

    if not scripts_to_run:
        print("No scripts found to execute in the analysis scripts directory.")
        return

    failed = []
    for script in scripts_to_run:
        print(f"Running '{script}'...")
        if not run_script(script):
            failed.append(script)
    if failed:
        print(
            f"Analysis failed for: {', '.join(failed)}. Do not use old output files for these analyses."
        )
        sys.exit(1)


if __name__ == "__main__":
    main()
