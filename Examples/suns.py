import argparse
import os
import subprocess

def file_exists(filepath):
    """Check if the file exists at the given filepath."""
    return os.path.isfile(filepath)

def parse_args():
    parser = argparse.ArgumentParser(description='Process a file with park or unpack options.')
    parser.add_argument('-f', '--file', type=str, required=True, help='Path to the file')
    parser.add_argument('-c', '--chunk', type=str, help='Chunk size')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-s', '--split', action='store_true', help='Split up the file option')
    group.add_argument('-u', '--unsplit', action='store_true', help='Repack the split files option')

    return parser.parse_args()

if __name__ == '__main__':
    args = parse_args()
        
    if args.split:
        print("Splitting...")
        if file_exists(args.file):
            print(f"File '{args.file}' exists. Spitting....")
            
            # Run a command and capture its output
            result = subprocess.run(['split', '-d', '-b', str(args.chunk), str(args.file), str(args.file)+'.part'], capture_output=True, text=True)

            # Check if the command was successful
            if result.returncode == 0:
                print("Split executed successfully:")
            else:
                print("Split failed with error:")
                print(result.stderr)
        else:
            print(f"File '{args.file}' does not exist. Cannot Split")
    elif args.unsplit:
        print("Unsplitting....")
        result = subprocess.run("cat *.part* > "+ str(args.file), shell=True, check=True)

        if result.returncode == 0:
            print("Unsplit executed successfully:")
        else:
            print("Unsplit failed with error:")
            print(result.stderr)



