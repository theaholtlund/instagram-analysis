"""List Instagram close friends."""

import sys
from pathlib import Path

# Allow scripts to import the shared package
sys.path.append(str(Path(__file__).resolve().parent.parent))

from instagram_analysis import variables
from instagram_analysis.export import account_names
from instagram_analysis.utils import write_to_file


def main():
    """Extract close friends and save the list."""
    path = Path(
        variables.DATA_DIR,
        variables.CONNECTIONS_DIR,
        variables.FOLLOWERS_DIR,
        "close_friends.html",
    )
    names = account_names(path)
    output = Path(variables.OUTPUT_DIR, "close_friends.txt")
    write_to_file(
        output,
        sorted(names, key=str.casefold),
        "Number of close friends",
        detailed=True,
        data_label="Users on close friends list",
    )
    print(f"Saved {len(names)} accounts to {output}.")


if __name__ == "__main__":
    main()
