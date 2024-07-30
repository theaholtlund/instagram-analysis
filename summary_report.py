# Import required libraries
import os
from utils import create_output_dir, get_script_dir

# Function to read lines from a file
def read_output_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.readlines()
    except FileNotFoundError:
        return None

# Function to parse a simple output file
def parse_simple_output(data):
    header = data[0].strip()
    return int(header.split(": ")[1]), []

# Function to parse a list output file
def parse_list_output(data):
    header = data[0].strip()
    count = int(header.split(": ")[1])
    items = [line.strip("- \n") for line in data[2:]]
    return count, items

# Function to parse the most liked output file
def parse_most_liked_output(data):
    header = data[0].strip()
    items = [line.strip("- \n") for line in data[1:] if line.strip()]
    return len(items), items

# Function to capitalise only the first word
def capitalize_first_word(text):
    if not text:
        return text
    return text[0].upper() + text[1:].lower()

# Function to generate a summary report from the various analysis output files
def generate_summary_report():
    script_dir = get_script_dir()
    output_dir = create_output_dir(script_dir)
    analysis_output_dir = os.path.join(script_dir, "analysis_outputs")
    summary_file_path = os.path.join(output_dir, "summary_report.txt")

    # Dictionary mapping filenames to their corresponding parser functions
    files_parsers = {
        "blocked_accounts.txt": parse_list_output,
        "close_friends.txt": parse_list_output,
        "count_comments.txt": parse_simple_output,
        "count_liked_comments.txt": parse_simple_output,
        "count_liked_posts.txt": parse_simple_output,
        "find_unfollowers.txt": parse_list_output,
        "most_liked_posts.txt": parse_most_liked_output
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

    # Write the summary report to a file
    with open(summary_file_path, "w", encoding="utf-8") as file:
        for file_name, (count, items) in summary_data.items():
            title = file_name.replace("_", " ").replace(".txt", "")
            title = capitalize_first_word(title)
            file.write(f"{title}: {count}\n")
            if items:
                for item in items:
                    file.write(f"- {item}\n")
                file.write("\n")
            elif "count" in title.lower():
                file.write("\n")

# Main function to coordinate execution of the script
if __name__ == "__main__":
    generate_summary_report()
