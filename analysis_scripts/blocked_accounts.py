import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
from instagram_analysis import variables
from instagram_analysis.utils import write_to_file
from instagram_analysis.export import account_names

def main():
    path = Path(variables.DATA_DIR, variables.CONNECTIONS_DIR, variables.FOLLOWERS_DIR, 'blocked_profiles.html')
    names = account_names(path)
    output = Path(variables.OUTPUT_DIR, 'blocked_accounts' + '.txt')
    write_to_file(output, sorted(names, key=str.casefold), 'Number of blocked accounts', detailed=True, data_label='Blocked accounts')
    print(f"Saved {len(names)} accounts to {output}.")

if __name__ == '__main__':
    main()
