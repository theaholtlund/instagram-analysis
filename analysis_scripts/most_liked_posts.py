"""Find the accounts whose posts received the most likes."""

import sys
from collections import Counter
from pathlib import Path

# Allow scripts to import the shared package
sys.path.append(str(Path(__file__).resolve().parent.parent))

from instagram_analysis import variables
from instagram_analysis.export import liked_post_owner, records
from instagram_analysis.utils import write_to_file


def main():
    """Find and save the accounts whose posts were liked most."""
    path = Path(
        variables.DATA_DIR,
        variables.ACTIVITY_DIR,
        variables.LIKES_DIR,
        variables.LIKED_POSTS_FILE,
    )
    counts = Counter()
    total = missing = 0
    for record in records(path):
        total += 1
        owner = liked_post_owner(record)
        if owner:
            counts[owner.casefold()] += 1
        else:
            missing += 1
    output = Path(variables.OUTPUT_DIR, "most_liked_posts.txt")
    lines = [f"- {name}: {count}" for name, count in counts.most_common(5)]
    lines.append(
        f"- {missing} of {total} liked posts have no identifiable owner in the export"
    )
    write_to_file(output, lines, header="Top 5 accounts whose posts you liked most:\n")
    print(
        f"Saved top accounts to {output}; {missing} of {total} posts have no identifiable owner."
    )


if __name__ == "__main__":
    main()
