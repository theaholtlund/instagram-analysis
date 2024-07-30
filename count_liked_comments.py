# Import required libraries
import os
from bs4 import BeautifulSoup
import variables
from utils import load_html_content, write_to_file_simple, create_output_dir, get_script_dir

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
    liked_comments_file = "liked_comments.html"
    file_path = os.path.join(likes_path, liked_comments_file)
    
    if os.path.exists(file_path):
        # Load the HTML content
        comments_html = load_html_content(file_path)
        
        # Parse the HTML content using BeautifulSoup
        comments_soup = BeautifulSoup(comments_html, "html.parser")
        
        # Extract likes from the HTML content
        likes = extract_likes(comments_soup)
        
        # Update the total likes count
        total_likes = len(likes)
        
        # Define output directory and create it if it does not exist
        output_dir = create_output_dir(script_dir)
        
        # Output the result to a file
        output_file_path = os.path.join(output_dir, "count_liked_comments.txt")
        write_to_file_simple(output_file_path, [total_likes], "Total number of likes given on Instagram comments")
        
        # Print out confirmation of file export
        print(f"The total number of likes given on comments by the user has been saved to '{output_file_path}'.")
    else:
        print(f"File '{liked_comments_file}' not found in the directory '{likes_path}'.")

if __name__ == "__main__":
    main()
