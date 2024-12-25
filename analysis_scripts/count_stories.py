# Import required libraries
import os
import sys
from pathlib import Path

# Ensure project root is in the path
project_root = Path(__file__).resolve().parent.parent
sys.path.append(str(project_root))

# Import modules and variables
import variables
from utils import get_script_dir, construct_file_path, write_to_file

def main():
    """Count the total number of files in the stories directory and save to a text file."""
    script_dir = get_script_dir()
    stories_path = construct_file_path(script_dir, variables.DATA_DIR, variables.MEDIA_DIR, variables.STORIES_DIR)
    
    # Count all files in the stories directory and its subdirectories
    total_files = sum(len(files) for _, _, files in os.walk(stories_path))
    
    # Construct output file path and output result to file
    output_file_path = construct_file_path(variables.OUTPUT_DIR, "count_stories.txt")
    write_to_file(output_file_path, [total_files], "Total number of files in stories: ", detailed=False)
    print(f"Total number of files in stories has been saved to '{output_file_path}'.")

if __name__ == "__main__":
    main()
