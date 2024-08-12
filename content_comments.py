# Import required libraries
import os
from collections import Counter
import variables
from utils import get_script_dir, construct_file_path, list_files_and_construct_paths, load_and_parse_html

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
    
    # Prepare the output data
    if top_repeated_comments:
        output_data = ["Top 5 repeated comments and the number of times they were made:"]
        for comment, count in top_repeated_comments:
            formatted_comment = comment.replace("Comment", "").strip()
            output_data.append(f"- {formatted_comment}, comment made {count} times")
    else:
        output_data = ["No repeated comments"]

    # Output the result to a file
    output_file_path = construct_file_path(variables.output_dir, "content_comments.txt")
    with open(output_file_path, "w") as f:
        f.write("\n".join(output_data) + "\n")
    
    # Print out confirmation of file export
    if top_repeated_comments:
        print(f"Top 5 repeated comments have been saved to '{output_file_path}'.")
    else:
        print(f"No repeated comments found. Status saved to '{output_file_path}'.")

if __name__ == "__main__":
    main()
