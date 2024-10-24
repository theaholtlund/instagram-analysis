# Import required libraries
import os
import sys

# Add project root directory to system path
script_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(script_dir)
sys.path.append(root_dir)

# Import modules and variables
import variables
from utils import get_script_dir, construct_file_path, write_to_file

def main():
    script_dir = get_script_dir()
    stories_path = construct_file_path(script_dir, variables.DATA_DIR, variables.MEDIA_DIR, variables.STORIES_DIR)
    
    # Count all files in the stories directory and its subdirectories
    total_files = sum(len(files) for _, _, files in os.walk(stories_path))
    
    # Construct output file path and output result to file
    output_file_path = construct_file_path(variables.OUTPUT_DIR, "count_stories.txt")
    write_to_file(output_file_path, [total_files], "Total number of files in stories: ", detailed=False)

if __name__ == "__main__":
    main()
