# Import required libraries
import sys
from pathlib import Path

# Ensure project root is in the path
project_root = Path(__file__).resolve().parent.parent
sys.path.append(str(project_root))

# Import modules and variables
import variables
from utils import get_script_dir, construct_file_path, load_and_parse_html, write_to_file, extract_content

def main():
    """Count the total number of liked posts and save to text file."""
    script_dir = get_script_dir()
    
    # Load, parse and extract liked posts from HTML content
    file_path = construct_file_path(script_dir, variables.DATA_DIR, variables.ACTIVITY_DIR, variables.LIKES_DIR, variables.LIKED_POSTS_FILE)
    likes_soup = load_and_parse_html(file_path)
    likes = extract_content(likes_soup, tag="a", content_type="href")
    
    # Update the total likes count
    total_likes = len(likes)
    
    # Construct output file path and output result to file
    output_file_path = construct_file_path(variables.OUTPUT_DIR, "count_liked_posts.txt")
    write_to_file(output_file_path, [total_likes], "Total number of likes given on Instagram: ", detailed=False)
    print(f"Number of likes given has been saved to '{output_file_path}'.")

if __name__ == "__main__":
    main()
