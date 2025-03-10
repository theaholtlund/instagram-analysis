# Import required libraries
import sys
import webbrowser
from pathlib import Path
from weasyprint import HTML

# Ensure project root is in the path
script_dir = Path(__file__).resolve().parent
project_root = script_dir.parent
sys.path.append(str(project_root))

# Import modules and variables
import variables
from utils import read_file, parse_simple_output, parse_list_output, parse_detailed_output
from create_plot import create_activity_plots, create_close_friends_plot

def generate_html_content(summary_data, show_count_files):
    """Generate HTML content for the summary report, including bar and pie charts."""
    analysis_output_dir = Path(variables.OUTPUT_DIR)
    report_content = [
        "<div class='container'>", 
        "<h2>Instagram Activity Summary</h2>\n",
        f"""
        <div class="chart-container">
            <h3>Total Likes and Comments</h3>
            <img src="../{analysis_output_dir / variables.PLOT_BAR_CHART}" alt="Total Likes and Comments">
            <h3>Likes-to-Comments Ratio</h3>
            <img src="../{analysis_output_dir / variables.PLOT_PIE_CHART}" alt="Likes-to-Comments Ratio">
            <h3>Close Friends Among Those Followed</h3>
            <img src="../{analysis_output_dir / variables.PLOT_FOLLOWING_CHART}" alt="Close Friends Among Those Followed">
        </div>
        """
    ]

    # Add summaries for each output file
    for file_name, (count, items) in summary_data.items():
        # Convert title to uppercase and format it
        title = file_name.replace("_", " ").replace(".txt", "").upper()
        
        # Add expandable details for file contents
        report_content.append(f"<h2>{title}: {count}</h2>\n" if file_name in show_count_files else f"<h2>{title}:</h2>\n")

        if items:
            item_list = "".join(f"<p>- {item}</p>\n" for item in items)
            report_content.append(f"""
                <details><summary>CLICK TO EXPAND</summary>
                    <div class='content-list'>{item_list}</div>
                </details>\n
            """)

    report_content.append("</div>")
    return "\n".join(report_content)

def export_to_pdf(summary_file_path, pdf_output_path):
    """Export the summary report HTML to a PDF file."""
    try:
        html_content = summary_file_path.read_text(encoding="utf-8")
        pdf = HTML(string=html_content).write_pdf()
        pdf_output_path.write_bytes(pdf)
        print(f"PDF report saved to {pdf_output_path}")
    except Exception as e:
        print(f"Error exporting to PDF: {e}")

def generate_summary_report():
    """Generate the HTML summary report with plots from analysis output files."""
    analysis_output_dir = Path(variables.OUTPUT_DIR)
    followers_file_dir = Path(variables.DATA_DIR, variables.CONNECTIONS_DIR, variables.FOLLOWERS_DIR)
    summary_file_path = script_dir / variables.SUMMARY_REPORT
    template_file_path = script_dir / variables.REPORT_TEMPLATE

    try:
        # Generate bar and pie charts with activity data
        create_activity_plots(
            comments_file=analysis_output_dir / "count_comments.txt",
            likes_file=analysis_output_dir / "count_liked_posts.txt"
        )

        # Generate following vs close friends plot
        create_close_friends_plot(
            close_friends_file=analysis_output_dir / "close_friends.txt",
            following_file=followers_file_dir / "following.html"
        )
    except Exception as e:
        print(f"Error creating plots: {e}")
        return

    # Define parsers for each file type
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
        for file_name, parser in files_parsers.items() if (analysis_output_dir / file_name).exists()
    }

    show_count_files = {"count_comments.txt", "count_liked_comments.txt", "count_liked_posts.txt", "count_stories.txt"}

    # Generate and read HTML template
    report_content = generate_html_content(summary_data, show_count_files)
    html_template = read_file(template_file_path)
    if not html_template:
        print("Error: Failed to load HTML template.")
        return

    # Write content into the template and save the report
    try:
        summary_file_path.write_text(html_template.replace("{{{content}}}", report_content), encoding="utf-8")
        print(f"The summary report has been generated and saved to '{summary_file_path}'.")

        # Open the report in a browser
        webbrowser.open(summary_file_path.as_uri())

        # Export the report in PDF format
        export_to_pdf(summary_file_path, analysis_output_dir / "instagram_report.pdf")
    except Exception as e:
        print(f"Error writing summary report: {e}")

if __name__ == "__main__":
    generate_summary_report()
