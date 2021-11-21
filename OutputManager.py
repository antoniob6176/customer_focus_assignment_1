import sys

class OutputManager():
    def __init__(self) -> None:
        pass # we can add different outputs here, ex: print to file or to http server
    def print(self, text, end = "\n"):
        print(text, end)

    def printOptions(self, text, options, selectedOption):
        print(text)
        padding = "                       "
        print("\n".join([f"{option}{padding}" if index != selectedOption else f"[{option}]{padding}" for index, option in enumerate(options)]))
        
    def clearOptions(self, lineCount):
        for i in range(lineCount):
            sys.stdout.write("\033[F")
        print("\r")