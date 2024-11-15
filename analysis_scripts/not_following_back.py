# Import required libraries
import os
import sys
from pathlib import Path

# Add project root directory to system path if not already present
script_dir = Path(__file__).resolve().parent
root_dir = script_dir.parent
if str(root_dir) not in sys.path:
    sys.path.append(str(root_dir))

# Import modules and variables
import variables
from utils import get_script_dir, construct_file_path, load_and_parse_html, write_to_file, extract_content

def main():
    """Identify accounts not following back and save the list to text file."""
    script_dir = get_script_dir()
    
    # Define base paths for the followers and following HTML files
    base_path = construct_file_path(script_dir, variables.DATA_DIR, variables.CONNECTIONS_DIR, variables.FOLLOWERS_DIR)
    
    # Construct paths for the followers and following HTML files
    followers_path = construct_file_path(base_path, variables.FOLLOWERS_FILE)
    following_path = construct_file_path(base_path, variables.FOLLOWING_FILE)
    
    # Parse the HTML content using BeautifulSoup
    followers_soup = load_and_parse_html(followers_path)
    following_soup = load_and_parse_html(following_path)
    
    if followers_soup is None or following_soup is None:
        print("Error loading or parsing HTML files.")
        return
    
    # Extract followers and following usernames
    followers_usernames = extract_content(followers_soup, tag="a", content_type="text")
    following_usernames = extract_content(following_soup, tag="a", content_type="text")
    
    # Find accounts the user is following that are not following them back
    not_following_back = following_usernames - followers_usernames
    
    # Construct output file path and output result to file
    output_file_path = construct_file_path(variables.OUTPUT_DIR, "not_following_back.txt")
    write_to_file(output_file_path, not_following_back, "Accounts not following back", detailed=True, data_label="Usernames not following back")
    print(f"Accounts not following back have been saved to '{output_file_path}'.")

if __name__ == "__main__":
    main()
