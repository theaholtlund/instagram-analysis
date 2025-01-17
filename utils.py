# Import required libraries
from pathlib import Path
from bs4 import BeautifulSoup

def get_script_dir():
    """Return the directory of the current script."""
    return Path(__file__).resolve().parent

def construct_file_path(*path_parts):
    """Construct a file path from the given parts."""
    return Path(*path_parts)

def list_files_and_construct_paths(directory):
    """List files in a directory and construct their full paths."""
    return [str(f) for f in Path(directory).iterdir() if f.is_file()]

def read_file(file_path, as_lines=False):
    """Read content from a file, returning either a string or a list of lines."""
    try:
        with Path(file_path).open("r", encoding="utf-8") as file:
            return file.readlines() if as_lines else file.read()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return []

def load_and_parse_html(file_path):
    """Load and parse HTML content from a file using BeautifulSoup."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return BeautifulSoup(file.read(), 'html.parser')
    except Exception as e:
        print(f"Error loading HTML file '{file_path}': {e}")
        return None

def extract_content(soup, tag, attr=None, text_condition=None, content_type="text"):
    """Extract content from HTML based on tag, attributes and optional text conditions."""
    elements = soup.find_all(tag, attrs=attr)
    extracted = set()

    for element in elements:
        if text_condition and text_condition not in element.get_text():
            continue
        content = element['href'].split("/_u/")[-1] if content_type == "href" else element.get_text()
        extracted.add(content)
    
    return extracted

def write_to_file(file_path, data, header="", detailed=False, data_label=None):
    """Write data to a file, with optional headers and detailed formatting."""
    file_path = Path(file_path)
    try:
        with file_path.open("w", encoding="utf-8") as file:
            if detailed:
                file.write(f"{header}: {len(data)}\n")
                file.write(f"{data_label}:\n")
                for item in data:
                    file.write(f"- {item}\n")
            else:
                if header:
                    file.write(f"{header}")
                for item in data:
                    file.write(f"{item}\n")
    except Exception as e:
        print(f"Error writing to file '{file_path}': {e}")

def parse_simple_output(data):
    """Parse a simple output file where the first line contains a count."""
    try:
        header = data[0].strip()
        count = int(header.split(": ")[1])
        return count, []
    except (IndexError, ValueError) as e:
        print(f"Error parsing simple output: {e}")
        return 0, []

def parse_list_output(data):
    """Parse a list output file with items starting from the third line."""
    try:
        header = data[0].strip()
        count = int(header.split(": ")[1])
        items = [line.strip("- \n") for line in data[2:]]
        return count, items
    except (IndexError, ValueError) as e:
        print(f"Error parsing list output: {e}")
        return 0, []

def parse_detailed_output(data):
    """Parse a detailed output file where items appear after the first line."""
    try:
        header = data[0].strip()
        items = [line.strip("- \n") for line in data[1:] if line.strip()]
        return len(items), items
    except IndexError as e:
        print(f"Error parsing detailed output: {e}")
        return 0, []
