# Import required libraries
import os
import sys
import webbrowser

# Add the project root directory to the system path
script_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(script_dir)
sys.path.append(root_dir)

# Import shared functionality
import variables
from utils import (read_file, construct_file_path, parse_simple_output, parse_list_output, parse_detailed_output, capitalise_first_word)

# Function to read the HTML template from a file
def read_html_template(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

# Function to generate a summary report from the various analysis output files
def generate_summary_report():
    # Define the directories based on the new structure
    analysis_output_dir = construct_file_path(root_dir, variables.output_dir)
    summary_file_path = construct_file_path(script_dir, "summary_report.html")
    template_file_path = construct_file_path(script_dir, "report_template.html")

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
    summary_data = {
        file_name: parser(read_file(construct_file_path(analysis_output_dir, file_name)))
        for file_name, parser in files_parsers.items()
    }

    # Files that should display a count after the title
    show_count_files = {"count_comments.txt", "count_liked_comments.txt", "count_liked_posts.txt"}

    # Generate HTML content for the report
    report_content = ""
    for file_name, (count, items) in summary_data.items():
        title = capitalise_first_word(file_name.replace("_", " ").replace(".txt", ""))
        report_content += f"<h2>{title}: {count}</h2>\n"

        if items:
            report_content += "<details><summary>Click to expand</summary>\n"
            report_content += "<div class='content-list'>\n"
            for item in items:
                report_content += f"<p>- {item}</p>\n"
            report_content += "</div>\n</details>\n\n"

    # Read the HTML template
    html_template = read_html_template(template_file_path)

    # Write to the HTML file with content
    with open(summary_file_path, "w", encoding="utf-8") as file:
        file.write(html_template.format(content=report_content))

    # Print out confirmation of file export and open in browser
    print(f"The summary report has been generated and saved to '{summary_file_path}'.")
    webbrowser.open(f'file://{os.path.abspath(summary_file_path)}')

# Main function to coordinate execution of the script
if __name__ == "__main__":
    generate_summary_report()
