"""Count comments on Instagram posts and reels."""

import sys
from pathlib import Path

# Allow scripts to import the shared package
sys.path.append(str(Path(__file__).resolve().parent.parent))

from instagram_analysis import variables
from instagram_analysis.export import comments
from instagram_analysis.utils import write_to_file


def main():
    """Count and save comments on posts and reels."""
    directory = Path(variables.DATA_DIR, variables.ACTIVITY_DIR, variables.COMMENTS_DIR)
    paths = sorted(directory.glob("post_comments*.html")) + sorted(
        directory.glob("reels_comments*.html")
    )
    if not paths:
        raise FileNotFoundError(f"No post or reel comment files found in {directory}")
    count = sum(1 for path in paths for _ in comments(path))
    output = Path(variables.OUTPUT_DIR, "count_comments.txt")
    write_to_file(output, [count], "Total number of comments on posts and reels: ")
    print(f"Saved {count} comments to {output}.")


if __name__ == "__main__":
    main()
