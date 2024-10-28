# Import required libraries
import sys
import webbrowser
from pathlib import Path

# Add the project root directory to the system path if not already present
script_dir = Path(__file__).resolve().parent
root_dir = script_dir.parent
if str(root_dir) not in sys.path:
    sys.path.append(str(root_dir))

# Import modules and variables
import variables
from utils import read_file, parse_simple_output, parse_list_output, parse_detailed_output

# Function to generate HTML content for the report
def generate_html_content(summary_data, show_count_files):
    """Generate HTML content for the summary report."""
    report_content = ""
    
    for file_name, (count, items) in summary_data.items():
        # Convert title to uppercase and format it
        title = file_name.replace("_", " ").replace(".txt", "").upper()
        
        # Add count to the title if applicable
        report_content += f"<h2>{title}: {count}</h2>\n" if file_name in show_count_files else f"<h2>{title}:</h2>\n"

        # Expandable details for file contents
        if items:
            report_content += (
                "<details><summary>CLICK TO EXPAND</summary>\n"
                "<div class='content-list'>\n" +
                "".join(f"<p>- {item}</p>\n" for item in items) +
                "</div>\n</details>\n\n"
            )

    return report_content

# Function to generate a summary report from analysis output files
def generate_summary_report():
    """Generate the HTML summary report from analysis output files."""
    analysis_output_dir = Path(variables.OUTPUT_DIR)
    summary_file_path = script_dir / variables.SUMMARY_REPORT
    template_file_path = script_dir / variables.REPORT_TEMPLATE

    # Map filenames to parser functions
    files_parsers = {
        "blocked_accounts.txt": parse_list_output,
        "close_friends.txt": parse_list_output,
        "content_comments.txt": parse_detailed_output,
        "count_comments.txt": parse_simple_output,
        "count_liked_comments.txt": parse_simple_output,
        "count_liked_posts.txt": parse_simple_output,
        "count_stories.txt": parse_simple_output,
        "most_liked_posts.txt": parse_detailed_output,
        "not_following_back.txt": parse_list_output
    }

    # Parse each file and store results
    summary_data = {
        file_name: parser(read_file(analysis_output_dir / file_name, as_lines=True))
        for file_name, parser in files_parsers.items()
        if (analysis_output_dir / file_name).exists()
    }

    # Files that should display a count after the title
    show_count_files = {"count_comments.txt", "count_liked_comments.txt", "count_liked_posts.txt", "count_stories.txt"}

    # Generate and read HTML template
    report_content = generate_html_content(summary_data, show_count_files)
    html_template = read_file(template_file_path)

    if html_template is None:
        print("Error: Failed to load HTML template.")
        return

    # Write content into the template and save the report
    summary_file_path.write_text(html_template.replace("{{{content}}}", report_content), encoding="utf-8")

    # Confirmation and automatic report opening
    print(f"The summary report has been generated and saved to '{summary_file_path}'.")
    webbrowser.open(summary_file_path.as_uri())

if __name__ == "__main__":
    generate_summary_report()
