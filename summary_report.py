# Import required libraries
import os
import variables
from utils import get_script_dir, read_output_file, parse_simple_output, parse_list_output, parse_detailed_output, capitalise_first_word

# Function to generate a summary report from the various analysis output files
def generate_summary_report():
    script_dir = get_script_dir()
    analysis_output_dir = os.path.join(script_dir, "analysis_outputs")
    summary_file_path = os.path.join(variables.output_dir, "summary_report.md")

    # Dictionary mapping filenames to their corresponding parser functions
    files_parsers = {
        "blocked_accounts.txt": parse_list_output,
        "close_friends.txt": parse_list_output,
        "content_comments.txt": parse_detailed_output,
        "count_comments.txt": parse_simple_output,
        "count_liked_comments.txt": parse_simple_output,
        "count_liked_posts.txt": parse_simple_output,
        "most_liked_posts.txt": parse_detailed_output,
        "not_following_back.txt": parse_list_output
    }

    # Dictionary to store parsed data from each file
    summary_data = {}

    # Loop through each file, parse the data and store in summary data dictionary
    for file_name, parser in files_parsers.items():
        file_path = os.path.join(analysis_output_dir, file_name)
        data = read_output_file(file_path)
        if data:
            count, items = parser(data)
            summary_data[file_name] = (count, items)
        else:
            summary_data[file_name] = (0, [])

    # Write the summary report to a Markdown file
    with open(summary_file_path, "w", encoding="utf-8") as file:
        file.write("# Analysis Summary Report\n")
        file.write("\n")

        for file_name, (count, items) in summary_data.items():
            title = file_name.replace("_", " ").replace(".txt", "")
            title = capitalise_first_word(title)
            file.write(f"## {title}: {count}\n\n")
            
            if items:
                file.write("<details><summary>Click to expand</summary>\n\n")
                for item in items:
                    file.write(f"- {item}\n")
                file.write("\n</details>\n\n")
        
        file.write("## End of summary report\n")

# Main function to coordinate execution of the script
if __name__ == "__main__":
    generate_summary_report()
