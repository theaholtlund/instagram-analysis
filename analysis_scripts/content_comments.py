# Import required libraries
import os
import sys
from collections import Counter

# Add the project root directory to the system path
script_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(script_dir)
sys.path.append(root_dir)

# Import the required modules
import variables
from utils import get_script_dir, construct_file_path, list_files_and_construct_paths, load_and_parse_html, write_to_file

# Function to extract comments
def extract_comments(soup):
    return [comment.text for comment in soup.find_all("td", class_="_2pin _a6_q") if "Comment" in comment.text]

# Main function to coordinate execution of the script
def main():
    script_dir = get_script_dir()
    
    # Define the path for the comments folder
    comments_path = construct_file_path(script_dir, variables.data_dir, variables.activity_dir, variables.comments_dir)
    
    # List files in the comments directory
    file_paths = list_files_and_construct_paths(comments_path)

    # Initialise the comment list
    all_comments = []
    
    # Iterate over all files in the comments directory
    for filename in file_paths:
        file_path = construct_file_path(comments_path, filename)
        
        # Parse the HTML content using BeautifulSoup
        comments_soup = load_and_parse_html(file_path)
        
        # Extract comments from the HTML content
        comments = extract_comments(comments_soup)
        
        # Add extracted comments to the list of all comments
        all_comments.extend(comments)
    
    # Count the frequency of each comment
    comment_counts = Counter(all_comments)
    
    # Filter out comments that were repeated more than once
    repeated_comments = {comment: count for comment, count in comment_counts.items() if count > 1}
    
    # Sort repeated comments by frequency in descending order and take the top 5
    top_repeated_comments = sorted(repeated_comments.items(), key=lambda x: x[1], reverse=True)[:5]
    
    # Prepare the output data with proper formatting
    output_data = ["Top 5 repeated comments and the number of times they were made:"]
    for comment, count in top_repeated_comments:
        formatted_comment = f"- {comment.replace('Comment', '').strip()}, comment made {count} times"
        output_data.append(formatted_comment)

    # Output the result to a file using write_to_file
    output_file_path = construct_file_path(variables.output_dir, "content_comments.txt")
    
    # Write the output with proper formatting
    write_to_file(output_file_path, data=output_data, header="", detailed=False)
    
    # Print out confirmation of file export
    message = (f"Top repeated comments have been saved to '{output_file_path}'."
               if top_repeated_comments else
               f"No repeat comments found, status saved to '{output_file_path}'.")
    print(message)

if __name__ == "__main__":
    main()
