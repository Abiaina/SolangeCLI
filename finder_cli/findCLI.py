import argparse
import os

finder = argparse.ArgumentParser(description='Find files and directories that match input criteria in current directory.')

finder.add_argument("search", metavar='match', type=str, help="Search criteria.")

args = vars(finder.parse_args())

for files_dirs in os.listdir('./'):
    if args['search'] in files_dirs:
        print(files_dirs)