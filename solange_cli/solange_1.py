import argparse

solange_cli = argparse.ArgumentParser(description='Process Solange music requests.')

solange_cli.add_argument('-a', "--album", required=False, help="Get lyric from recent Solange album provided")
solange_cli.add_argument('-s', "--song", required=False, help="Get lyric from recent Solange song provided")
solange_cli.add_argument('-t', "--tempo", required=False, help="Get lyrics from the Solange by tempo. Expects 'fast' or 'slow'.")
solange_cli.add_argument('low', help="Get lyrics in lowercase.")
solange_cli.add_argument('up', help="Get lyrics in uppercase.")

args = vars(solange_cli.parse_args())
print(args)
# print(f"Solange song requested {args['name']}", f"Solange song requested {args['name']}") 