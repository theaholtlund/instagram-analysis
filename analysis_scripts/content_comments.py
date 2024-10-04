# Import required libraries
import os
import sys
from collections import Counter

# Add project root directory to system path
script_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(script_dir)
sys.path.append(root_dir)

# Import the required modules
import variables
from utils import get_script_dir, construct_file_path, list_files_and_construct_paths, load_and_parse_html, write_to_file

# Function to extract comments
def extract_comments(soup):
    return [comment.text for comment in soup.find_all("td", class_="_2pin _a6_q") if "Comment" in comment.text]

def main():
    script_dir = get_script_dir()
    
    # Get files from comments folder
    comments_path = construct_file_path(script_dir, variables.DATA_DIR, variables.ACTIVITY_DIR, variables.COMMENTS_DIR)
    file_paths = list_files_and_construct_paths(comments_path)

    # Initialise the comment list
    all_comments = []
    
    # Iterate over all files in the comments directory
    for filename in file_paths:
        # Load, parse and extract comments from HTML content
        file_path = construct_file_path(comments_path, filename)
        comments_soup = load_and_parse_html(file_path)
        comments = extract_comments(comments_soup)
        
        # Add extracted comments to the list of all comments
        all_comments.extend(comments)
    
    # Count the frequency of each comment
    comment_counts = Counter(all_comments)
    
    # Filter out repeated comments and select top 5 by frequency in descending order
    repeated_comments = {comment: count for comment, count in comment_counts.items() if count > 1}
    top_repeated_comments = sorted(repeated_comments.items(), key=lambda x: x[1], reverse=True)[:5]
    
    # Prepare output data with proper formatting
    header = "Top 5 repeated comments and the number of times they were made:"
    output_data = [f"- {comment.replace('Comment', '').strip()}, comment made {count} times" for comment, count in top_repeated_comments]
    formatted_header = f"{header}\n"
    
    # Construct output file path and output result to file
    output_file_path = construct_file_path(variables.OUTPUT_DIR, "content_comments.txt")
    write_to_file(output_file_path, data=output_data, header=formatted_header, detailed=False)
    print(f"{'Top repeated comments have been saved' if top_repeated_comments else 'No repeat comments found, status saved'} to '{output_file_path}'.")

if __name__ == "__main__":
    main()
