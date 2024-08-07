# Import required libraries
import os
from bs4 import BeautifulSoup
import variables
from utils import get_script_dir, read_file, load_and_parse_html, write_to_file_simple

# Function to extract likes
def extract_likes(soup):
    return [like for like in soup.find_all("a", href=True) if like.text == "👍"]

# Main function to coordinate execution of the script
def main():
    script_dir = get_script_dir()
    
    # Define the path for the likes folder
    likes_path = os.path.join(script_dir, variables.data_dir, variables.activity_dir, variables.likes_dir)
    
    # Initialise the likes count
    total_likes = 0
    
    # Define the filename to process
    liked_posts_file = "liked_posts.html"
    file_path = os.path.join(likes_path, liked_posts_file)
    
    if os.path.exists(file_path):
        # Load the HTML content
        likes_html = read_file(file_path, "all")
        
        # Parse the HTML content using BeautifulSoup
        likes_soup = load_and_parse_html(file_path)
        
        # Extract likes from the HTML content
        likes = extract_likes(likes_soup)
        
        # Update the total likes count
        total_likes = len(likes)
        
        # Output the result to a file
        output_file_path = os.path.join(variables.output_dir, "count_liked_posts.txt")
        write_to_file_simple(output_file_path, [total_likes], "Total number of likes given on Instagram")
        
        # Print out confirmation of file export
        print(f"The total number of likes given by the user has been saved to '{output_file_path}'.")

if __name__ == "__main__":
    main()
