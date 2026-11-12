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
    count = sum(1 for path in paths for _ in comments(path))
    output = Path(variables.OUTPUT_DIR, 'count_comments.txt')
    write_to_file(output, [count], 'Total number of comments on posts and reels: ')
    print(f'Saved {count} comments to {output}.')

if __name__ == '__main__':
    main()
