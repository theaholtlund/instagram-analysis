import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
from instagram_analysis import variables
from instagram_analysis.utils import write_to_file
from instagram_analysis.export import comments

def main():
    directory = Path(variables.DATA_DIR, variables.ACTIVITY_DIR, variables.COMMENTS_DIR)
    paths = sorted(directory.glob('post_comments*.html')) + sorted(directory.glob('reels_comments*.html'))
    if not paths:
        raise FileNotFoundError(f'No post or reel comment files found in {directory}')
    from collections import Counter
    counts = Counter(comment for path in paths for comment in comments(path))
    lines = [f'- {comment}, comment made {count} times' for comment, count in counts.most_common() if count > 1][:5]
    output = Path(variables.OUTPUT_DIR, 'content_comments.txt')
    write_to_file(output, lines, 'Top 5 repeated comments on posts and reels:\n')
    print(f'Saved repeated comments to {output}.')

if __name__ == '__main__':
    main()
