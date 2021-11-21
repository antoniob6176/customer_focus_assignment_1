"""
this is the main CLI loop that shows users options and get the input
what's special is the interactive selection that can be used with the arrow keys
"""

import json
from FileManager import FileManager
from InputManager import InputManager

from LogManager import LogManager
from OutputManager import OutputManager

class CliManager():
    def __init__(self,
                logManager: LogManager,
                fileManager: FileManager,
                inputManager: InputManager,
                outputManager:OutputManager) -> None:

        self.logManager = logManager
        self.fileManager = fileManager
        self.inputManager = inputManager
        self.outputManager = outputManager

        self.actions = { # keeping everything isolated on the instance
            "help": {"function": self.getHelp, "description": "shows functions and descriptions"},
            "get stats": {"function": self.getStats, "description": "get the total statistics about a file"},
            "get percentage": {"function": self.getPercentage, "description": "give the percentage a values appeared in a field"},
            "get counts": {"function": self.getCounts, "description": "give the count of unique values that appeared in a field"},
            "add files": {"function": self.addFiles, "description": "adds files and can take a wildcard ex ./**/*.log"},
            "quit": {"function": self.quit, "description": "exits the program"},
        }

    def addFiles(self):
        value = self.inputManager.input("please type the path: ")
        self.fileManager.addFiles(value)

    def start(self):
        shouldContinue = True
        while shouldContinue:
            try:
                selected = self.getSelection(self.actions, "please select action: ")

                self.outputManager.print("")

                result = self.actions[selected]["function"]()
                if result:
                    self.outputManager.print(result)
                    self.inputManager.input("press enter to continue")
                shouldContinue = result != False
            except ValueError as ex:
                self.outputManager.printError(f"{type(ex).__name__}: {ex} not found")
            except KeyError as ex:
                self.outputManager.printError(f"{type(ex).__name__}: {ex} not found")
            except IndexError as ex:
                self.outputManager.printError(f"{type(ex).__name__}: {ex}")

    def getSelection(self, actions: dict, text="please select: \t"):
        if not actions:
            raise IndexError("no values are found, please add some")

        selectedAction = 0
        while True:
            self.outputManager.printOptions(text, actions, selectedAction)

            inputKey = self.inputManager.getKey()
            if inputKey == "right":
                selectedAction += 1
            elif inputKey == "left":
                selectedAction -= 1
            else:
                break

            selectedAction = min(selectedAction, len(actions) - 1)
            selectedAction = max(selectedAction, 0)
            self.outputManager.clearOptions(len(actions) + 2)

        return list(actions)[selectedAction]

    def getPercentage(self):
        field = self.getSelection(self.logManager.compiledData, "please select field: ")
        value = self.inputManager.input("please type the value that you want: ")

        percentage = self.logManager.getLogPercentage(field, value)

        return f"percentage of {value} is { int(percentage * 100)}%"

    def getCounts(self):
        field = self.getSelection(self.logManager.compiledData, "please select field: ")
        logCounts = self.logManager.getLogCounts(field)
        return f"logs per {field} is {json.dumps(logCounts, indent=2)}"

    def getStats(self):
        return json.dumps(self.logManager.compiledData, indent= 2)

    def getHelp(self):
        listToPrint = [f"{key}: {value['description']}" for key, value in self.actions.items()]
        return "\n".join(listToPrint) + "\n\nuse the arrow keys to navigate"

    def quit(self):
        return False
