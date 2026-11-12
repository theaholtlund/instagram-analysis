import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
from instagram_analysis import variables
from instagram_analysis.utils import write_to_file
from instagram_analysis.export import records

def main():
    path = Path(variables.DATA_DIR, variables.ACTIVITY_DIR, variables.LIKES_DIR, variables.LIKED_POSTS_FILE)
    count = sum(1 for _ in records(path))
    output = Path(variables.OUTPUT_DIR, 'count_liked_posts.txt')
    write_to_file(output, [count], 'Total number of liked posts: ')
    print(f'Saved {count} liked posts to {output}.')

if __name__ == '__main__':
    main()
