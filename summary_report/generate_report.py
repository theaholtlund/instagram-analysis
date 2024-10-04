# Import required libraries
import os
import sys
import webbrowser

# Add the project root directory to the system path
script_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(script_dir)
sys.path.append(root_dir)

# Import modules and variables
import variables
from utils import read_file, construct_file_path, parse_simple_output, parse_list_output, parse_detailed_output

# Function to generate HTML content for the report
def generate_html_content(summary_data, show_count_files):
    report_content = ""
    for file_name, (count, items) in summary_data.items():
        # Convert entire title to upper case
        title = file_name.replace("_", " ").replace(".txt", "").upper()

        # Show count in the title if applicable
        if file_name in show_count_files:
            report_content += f"<h2>{title}: {count}</h2>\n"
        else:
            report_content += f"<h2>{title}:</h2>\n"

        # Expandable details for file contents
        if items:
            report_content += "<details><summary>CLICK TO EXPAND</summary>\n"
            report_content += "<div class='content-list'>\n"
            for item in items:
                report_content += f"<p>- {item}</p>\n"
            report_content += "</div>\n</details>\n\n"
    
    return report_content

# Function to generate a summary report from analysis output files
def generate_summary_report():
    # Define directories and paths
    analysis_output_dir = construct_file_path(root_dir, variables.OUTPUT_DIR)
    summary_file_path = construct_file_path(script_dir, "summary_report.html")
    template_file_path = construct_file_path(script_dir, "report_template.html")

    # Map filenames to parser functions
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

    # Parse each file and store results
    summary_data = {
        file_name: parser(read_file(construct_file_path(analysis_output_dir, file_name), as_lines=True))
        for file_name, parser in files_parsers.items()
    }

    # Files that should display a count after the title
    show_count_files = {"count_comments.txt", "count_liked_comments.txt", "count_liked_posts.txt"}

    # Generate and read HTML template
    report_content = generate_html_content(summary_data, show_count_files)
    html_template = read_file(template_file_path)

    # Write content into the template and save the report
    with open(summary_file_path, "w", encoding="utf-8") as file:
        file.write(html_template.replace("{{{content}}}", report_content))

    # Confirmation and automatic report opening
    print(f"The summary report has been generated and saved to '{summary_file_path}'.")
    webbrowser.open(f'file://{os.path.abspath(summary_file_path)}')

if __name__ == "__main__":
    generate_summary_report()
