"""Find followed accounts that do not follow back."""

import sys
from pathlib import Path

# Allow scripts to import the shared package
sys.path.append(str(Path(__file__).resolve().parent.parent))

from instagram_analysis import variables
from instagram_analysis.export import account_names
from instagram_analysis.utils import write_to_file


def main():
    """Find and save accounts that do not follow back."""
    base = Path(variables.DATA_DIR, variables.CONNECTIONS_DIR, variables.FOLLOWERS_DIR)
    files = sorted(base.glob("followers_*.html"))
    if not files:
        raise FileNotFoundError(f"No followers_*.html files found in {base}")
    followers = set().union(*(account_names(path) for path in files))
    following = account_names(base / variables.FOLLOWING_FILE)
    follower_keys = {name.casefold() for name in followers}
    missing = sorted(
        (name for name in following if name.casefold() not in follower_keys),
        key=str.casefold,
    )
    output = Path(variables.OUTPUT_DIR, "not_following_back.txt")
    write_to_file(
        output,
        missing,
        "Accounts not following back",
        detailed=True,
        data_label="Usernames not following back",
    )
    print(f"Saved {len(missing)} accounts to {output}.")


if __name__ == "__main__":
    main()
