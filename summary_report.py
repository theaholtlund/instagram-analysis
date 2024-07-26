import os
from utils import create_output_dir, get_script_dir

def read_output_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.readlines()
    except FileNotFoundError:
        return None

def parse_simple_output(data):
    header = data[0].strip()
    return int(header.split(": ")[1]), []

def parse_list_output(data):
    header = data[0].strip()
    count = int(header.split(": ")[1])
    items = [line.strip("- \n") for line in data[2:]]
    return count, items

def parse_most_liked_output(data):
    header = data[0].strip()
    items = [line.strip("- \n") for line in data[1:] if line.strip()]
    return len(items), items

def generate_summary_report():
    script_dir = get_script_dir()
    output_dir = create_output_dir(script_dir)
    analysis_output_dir = os.path.join(script_dir, "analysis_outputs")
    summary_file_path = os.path.join(output_dir, "summary_report.txt")

    files_parsers = {
        "Blocked_accounts.txt": parse_list_output,
        "Close_friends.txt": parse_list_output,
        "Count_comments.txt": parse_simple_output,
        "Count_liked_posts.txt": parse_simple_output,
        "Find_unfollowers.txt": parse_list_output,
        "Most_liked_posts.txt": parse_most_liked_output
    }

    summary_data = {}

    for file_name, parser in files_parsers.items():
        file_path = os.path.join(analysis_output_dir, file_name)
        data = read_output_file(file_path)
        if data:
            count, items = parser(data)
            summary_data[file_name] = (count, items)
        else:
            summary_data[file_name] = (0, [])

    with open(summary_file_path, "w", encoding="utf-8") as file:
        for file_name, (count, items) in summary_data.items():
            title = file_name.replace("_", " ").replace(".txt", "").title()
            if "Count" in title:
                file.write(f"{title}: {count}\n")
            else:
                file.write(f"{title}: {count}\n")
                for item in items:
                    file.write(f"- {item}\n")
                file.write("\n")

if __name__ == "__main__":
    generate_summary_report()
