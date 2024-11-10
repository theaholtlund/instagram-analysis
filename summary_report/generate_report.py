# Import required libraries
import sys
import webbrowser
from pathlib import Path

# Add project root directory to system path
script_dir = Path(__file__).resolve().parent
root_dir = script_dir.parent
sys.path.append(str(root_dir)) if str(root_dir) not in sys.path else None

# Import modules and variables
import variables
from utils import read_file, parse_simple_output, parse_list_output, parse_detailed_output
from create_plot import create_activity_plot

def generate_html_content(summary_data, show_count_files, bar_chart_path, pie_chart_path):
    """Generate HTML content for the summary report, including bar and pie charts."""
    report_content = "<div class='container'>"
    analysis_output_dir = Path(variables.OUTPUT_DIR)

    # Add the bar chart and pie chart to the report
    report_content += "<h2>Instagram Activity Summary</h2>\n"
    report_content += f'<img src="../{analysis_output_dir/bar_chart_path.name}" alt="Total Likes and Comments" style="width:60%; margin:auto; display:block;">\n'
    report_content += f'<img src="../{analysis_output_dir/pie_chart_path.name}" alt="Likes-to-Comments Ratio" style="width:60%; margin:auto; display:block;">\n'

    # Add summaries for each output file
    for file_name, (count, items) in summary_data.items():
        # Convert title to uppercase and format it
        title = file_name.replace("_", " ").replace(".txt", "").upper()
        
        # Add count to the title if applicable
        report_content += f"<h2>{title}: {count}</h2>\n" if file_name in show_count_files else f"<h2>{title}:</h2>\n"
        
        # Add expandable details for file contents
        if items:
            report_content += (
                "<details><summary>CLICK TO EXPAND</summary>\n"
                "<div class='content-list'>\n"
                + "".join(f"<p>- {item}</p>\n" for item in items)
                + "</div>\n</details>\n\n"
            )

    report_content += "</div>"
    return report_content

def generate_summary_report():
    """Generate the HTML summary report with plots from analysis output files."""
    analysis_output_dir = Path(variables.OUTPUT_DIR)
    summary_file_path = script_dir / variables.SUMMARY_REPORT
    template_file_path = script_dir / variables.REPORT_TEMPLATE
    bar_chart_path = analysis_output_dir / "activity_chart_bar.png"
    pie_chart_path = analysis_output_dir / "activity_chart_pie.png"

    # Generate bar and pie charts with activity data
    create_activity_plot(
        output_path=bar_chart_path,
        comments_file=analysis_output_dir / "count_comments.txt",
        likes_file=analysis_output_dir / "count_liked_posts.txt"
    )

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
    report_content = generate_html_content(summary_data, show_count_files, bar_chart_path, pie_chart_path)
    html_template = read_file(template_file_path)

    if html_template is None:
        print("Error: Failed to load HTML template.")
        return

    # Write content into the template and save the report
    try:
        summary_file_path.write_text(html_template.replace("{{{content}}}", report_content), encoding="utf-8")
        print(f"The summary report has been generated and saved to '{summary_file_path}'.")
        webbrowser.open(summary_file_path.as_uri())
    except Exception as e:
        print(f"Error writing the summary report: {e}")

if __name__ == "__main__":
    generate_summary_report()
