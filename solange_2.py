import sys

cli_input = sys.argv
cli_output = ""
cli_option_variables = {
    "song": "",
    "album": "",
    "tempo": ""
}
cli_files_to_read = []

# Hardcoded Responses for CLI arguments.
# TODO: Make these responsive and pull from DB of solange music.
cli_argument_logic = {
    "up": "I just wanna wake to the sun",
    "binz": "sun down wind chimes...dollars never show up on cp time",
    "seat at the table": "sun down wind chimes...dollars never show up on cp time",
    "down": "don't touch my hair"
}

# Handles help statment of solange cli.
if "-h" in cli_input or "-help" in cli_input:
    print("Welcome to the Solange CLI for her later works!")
    print("Arguments: random, up, low")
    print("random : returns a random solange lyric")
    print("up : returns lyrics in uppercase")
    print("low : returns lyrics in lowercase")
    print("Optional Arguments: -song, -album, -tempo")
    print("-song :  prints lyric from recent Solange song provided")
    print("-album : prints lyric from recent Solange album provided")
    print("-tempo : expects input of 'fast' or 'slow' prints lyric from modern Solange song that matches tempo")
    print("Positional Arguments: Takes a list of file names")
    print("example positional arugment: *music.txt solange.txt")
    print("Example Solange CLI arguments")
    print("python solange_2.py random up -song")
else:  
    # Set Flag Arguments as variables.
    first_positional_argument_index = 0
    for index,v in enumerate(cli_input): 
        if "-" in v and (index + 1) < len(cli_input):
            cli_option_variables[v[1:]] = cli_input[(index + 1)]
            first_positional_argument_index = index + 2

    # Process Flag Argument variables.
    # Uses built in logic to process and set responses.
    for var in cli_option_variables:
        if cli_option_variables[var] != "" and cli_option_variables[var] in cli_argument_logic:
            cli_output += (cli_argument_logic[cli_option_variables[var]])

    # Gets list of files to read.
    cli_files_to_read = cli_input[first_positional_argument_index:]

    # Set Flag Arguments as variables.
    first_positional_argument_index = 0
    for index,v in enumerate(cli_input): 
        if "-" in v and (index + 1) < len(cli_input):
            cli_option_variables[v[1:]] = cli_input[(index + 1)]
            first_positional_argument_index = index + 2

    # Changes case of response.
    if "low" in cli_input:
        cli_output = cli_output.lower()
    if "up" in cli_input:
        cli_output = cli_output.upper()   

    print(cli_output)
    print("Files input to read:", cli_files_to_read)
