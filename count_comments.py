# Import required libraries
import os
from bs4 import BeautifulSoup
import config
from utils import load_html_content, write_to_file_simple, create_output_dir, get_script_dir

# Function to extract comments from the provided HTML content
def extract_comments(soup):
    return [comment.text for comment in soup.find_all("td", class_="_2pin _a6_q") if "Comment" in comment.text]

# Main function to coordinate execution of the script
def main():
    # Get the directory of the current script
    script_dir = get_script_dir()
    
    # Define the path for the comments folder
    comments_path = os.path.join(script_dir, config.data_dir, config.activity_dir, config.comments_dir)
    
    # Initialise the comment count
    total_comments = 0
    
    # Iterate over all files in the comments directory
    for filename in os.listdir(comments_path):
        file_path = os.path.join(comments_path, filename)
        
        # Load the HTML content
        comments_html = load_html_content(file_path)
        
        # Parse the HTML content using BeautifulSoup
        comments_soup = BeautifulSoup(comments_html, "html.parser")
        
        # Extract comments from the HTML content
        comments = extract_comments(comments_soup)
        
        # Update the total comment count
        total_comments += len(comments)
    
    # Define output directory and create it if it does not exist
    output_dir = create_output_dir(script_dir)
    
    # Output the result to a file
    output_file_path = os.path.join(output_dir, "count_comments.txt")
    write_to_file_simple(output_file_path, [total_comments], "Total number of comments left on Instagram")
    
    # Print out confirmation of file export
    print(f"The total number of comments left by the user has been saved to '{output_file_path}'.")

if __name__ == "__main__":
    main()
