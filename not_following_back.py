# Import required libraries
import os
import variables
from utils import get_script_dir, read_file, load_and_parse_html, write_to_file_detailed

# Function to extract usernames
def extract_usernames(soup):
    return {a.text for a in soup.find_all("a", href=True)}

# Main function to coordinate execution of the script
def main():
    script_dir = get_script_dir()
    
    # Define paths for the HTML files within the data files folder
    followers_path = os.path.join(script_dir, variables.data_dir, variables.connections_dir, variables.followers_dir, "followers_1.html")
    following_path = os.path.join(script_dir, variables.data_dir, variables.connections_dir, variables.followers_dir, "following.html")
    
    # Load the HTML content with error handling
    followers_html = read_file(followers_path, "all")
    following_html = read_file(following_path, "all")
    
    # Parse the HTML content using BeautifulSoup
    followers_soup = load_and_parse_html(followers_path)
    following_soup = load_and_parse_html(following_path)
    
    # Extract followers and following usernames
    followers_usernames = extract_usernames(followers_soup)
    following_usernames = extract_usernames(following_soup)
    
    # Find account names the user is following, that are not following them back
    not_following_back = following_usernames - followers_usernames
    
    # Output the result to a file
    output_file_path = os.path.join(variables.output_dir, "not_following_back.txt")
    write_to_file_detailed(output_file_path, not_following_back, "Accounts not following back", "Usernames not following back")
    
    # Print out confirmation of file export
    print(f"Accounts not following back have been saved to '{output_file_path}'.")

if __name__ == "__main__":
    main()
