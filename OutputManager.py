"""
handles printing to console and clearing some lines of it 
"""

import sys


class OutputManager():
    def __init__(self) -> None:
        pass  # we can add different outputs here, ex: print to file or to http server

    def print(self, text, end="\n"):
        print(text, end)

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
