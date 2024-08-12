# Import required libraries
import variables
from utils import get_script_dir, construct_file_path, list_files_and_construct_paths, load_and_parse_html, write_to_file_simple

# Function to extract comments
def extract_comments(soup):
    return [comment.text for comment in soup.find_all("td", class_="_2pin _a6_q") if "Comment" in comment.text]

# Main function to coordinate execution of the script
def main():
    script_dir = get_script_dir()
    
    # Define the path for the comments folder
    comments_path = construct_file_path(script_dir, variables.data_dir, variables.activity_dir, variables.comments_dir)
    
    # Initialise the comment count
    total_comments = 0
    
    # List files in the comments directory
    file_paths = list_files_and_construct_paths(comments_path)

    # Iterate over all files in the comments directory
    for filename in file_paths:
        file_path = construct_file_path(comments_path, filename)
        
        # Parse the HTML content using BeautifulSoup
        comments_soup = load_and_parse_html(file_path)
        
        # Extract comments from the HTML content
        comments = extract_comments(comments_soup)
        
        # Update the total comment count
        total_comments += len(comments)
    
    # Output the result to a file
    output_file_path = construct_file_path(variables.output_dir, "count_comments.txt")
    write_to_file_simple(output_file_path, [total_comments], "Total number of comments left on Instagram")
    
    # Print out confirmation of file export
    print(f"The total number of comments left by the user has been saved to '{output_file_path}'.")

if __name__ == "__main__":
    main()
