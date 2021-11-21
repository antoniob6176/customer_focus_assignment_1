"""
handles printing to console and clearing some lines of it 
"""

import sys

class bcolors:
    """https://stackoverflow.com/questions/287871/how-to-print-colored-text-to-the-terminal"""
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class OutputManager():
    def __init__(self) -> None:
        pass  # we can add different outputs here, ex: print to file or to http server

    def print(self, text, end="\n"):
        print(text, end)

    def printError(self, text, end="\n"):
        print(f"{bcolors.WARNING}{text}{bcolors.ENDC}", end)

    def printOptions(self, text, options, selectedOption):
        print(text)
        # paddin is needed to clean up the old characters
        padding = "                       "
        print("\n".join([f"{option}{padding}" if index !=
                         selectedOption else f"[{option}]{padding}" for index, option in enumerate(options)]))

    def clearOptions(self, lineCount):
        for _ in range(lineCount):
            # this makes the cursor go back up a few lines
            sys.stdout.write("\033[F")
        print("\r")
