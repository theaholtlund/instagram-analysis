# Import required libraries
import variables
from utils import get_script_dir, read_file, construct_file_path, parse_simple_output, parse_list_output, parse_detailed_output, capitalise_first_word
import os

# Function to generate a summary report from the various analysis output files
def generate_summary_report():
    script_dir = get_script_dir()
    analysis_output_dir = construct_file_path(script_dir, variables.output_dir)
    summary_file_path = construct_file_path(variables.output_dir, "summary_report.html")

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

    # HTML template for the report
    html_template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Analysis Summary Report</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 20px; }}
            h1, h2 {{ color: #2c3e50; }}
            details {{ margin: 10px 0; }}
            summary {{ cursor: pointer; font-weight: bold; }}
            .content-list {{ padding-left: 20px; }}
        </style>
    </head>
    <body>
        <h1>Analysis Summary Report</h1>
        {content}
        <h2>End of summary report</h2>
    </body>
    </html>
    """

    # Generate the HTML content
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

    # Write the HTML file
    with open(summary_file_path, "w", encoding="utf-8") as file:
        file.write(html_template.format(content=report_content))

    # Print out confirmation of file export and open in browser
    print(f"The summary report has been generated and saved to '{summary_file_path}'.")

# Main function to coordinate execution of the script
if __name__ == "__main__":
    generate_summary_report()
