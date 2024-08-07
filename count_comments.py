# Import required libraries
import os
import variables
from utils import get_script_dir, read_file, load_and_parse_html, write_to_file_simple

# Function to extract comments
def extract_comments(soup):
    return [comment.text for comment in soup.find_all("td", class_="_2pin _a6_q") if "Comment" in comment.text]

# Main function to coordinate execution of the script
def main():
    script_dir = get_script_dir()
    
    # Define the path for the comments folder
    comments_path = os.path.join(script_dir, variables.data_dir, variables.activity_dir, variables.comments_dir)
    
    # Initialise the comment count
    total_comments = 0
    
    # Iterate over all files in the comments directory
    for filename in os.listdir(comments_path):
        file_path = os.path.join(comments_path, filename)
        
        # Parse the HTML content using BeautifulSoup
        comments_soup = load_and_parse_html(file_path)
        
        # Extract comments from the HTML content
        comments = extract_comments(comments_soup)
        
        # Update the total comment count
        total_comments += len(comments)
    
    # Output the result to a file
    output_file_path = os.path.join(variables.output_dir, "count_comments.txt")
    write_to_file_simple(output_file_path, [total_comments], "Total number of comments left on Instagram")
    
    # Print out confirmation of file export
    print(f"The total number of comments left by the user has been saved to '{output_file_path}'.")

if __name__ == "__main__":
    main()
