# Import required libraries
import os
import sys

# Add project root directory to system path
script_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(script_dir)
sys.path.append(root_dir)

# Import modules and variables
import variables
from utils import get_script_dir, construct_file_path, list_files_and_construct_paths, load_and_parse_html, write_to_file

# Function to extract comments
def extract_comments(soup):
    """Extract comments from HTML content."""
    return [comment.text for comment in soup.find_all("td", class_="_2pin _a6_q") if "Comment" in comment.text]

def main():
    """Count the total number of comments made and save to text file."""
    script_dir = get_script_dir()
    
    # Get files from comments folder
    comments_path = construct_file_path(script_dir, variables.DATA_DIR, variables.ACTIVITY_DIR, variables.COMMENTS_DIR)
    file_paths = list_files_and_construct_paths(comments_path)
    
    # Initialise the comment count
    total_comments = 0

    # Iterate over all files in the comments directory
    for filename in file_paths:
        # Load, parse and extract comments from HTML content
        file_path = construct_file_path(comments_path, filename)
        comments_soup = load_and_parse_html(file_path)
        comments = extract_comments(comments_soup)
        
        # Update the total comment count
        total_comments += len(comments)
    
    # Construct output file path and output result to file
    output_file_path = construct_file_path(variables.OUTPUT_DIR, "count_comments.txt")
    write_to_file(output_file_path, [total_comments], "Total number of comments left on Instagram: ", detailed=False)
    print(f"Number of comments made has been saved to '{output_file_path}'.")

if __name__ == "__main__":
    main()
