# Import required libraries
import sys
from pathlib import Path

# Add project root directory to system path if not already present
script_dir = Path(__file__).resolve().parent
root_dir = script_dir.parent
if str(root_dir) not in sys.path:
    sys.path.append(str(root_dir))

# Import modules and variables
import variables
from utils import get_script_dir, construct_file_path, load_and_parse_html, write_to_file

# Function to extract likes
def extract_likes(soup):
    """Extract liked comments from HTML content."""
    return [like for like in soup.find_all("a", href=True) if like.text == "👍"]

def main():
    """Count the total number of likes given on comments and save to text file."""
    script_dir = get_script_dir()
    
    # Load, parse and extract liked comments from HTML content
    file_path = construct_file_path(script_dir, variables.DATA_DIR, variables.ACTIVITY_DIR, variables.LIKES_DIR, variables.LIKED_COMMENTS_FILE)
    comments_soup = load_and_parse_html(file_path)
    comment_likes = extract_likes(comments_soup)
    
    # Update the total likes count
    total_likes = len(comment_likes)
    
    # Construct output file path and output result to file
    output_file_path = construct_file_path(variables.OUTPUT_DIR, "count_liked_comments.txt")
    write_to_file(output_file_path, [total_likes], "Total number of likes given on Instagram comments: ", detailed=False)
    print(f"Number of likes given on comments has been saved to '{output_file_path}'.")

if __name__ == "__main__":
    main()
