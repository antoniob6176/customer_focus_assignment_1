import json
from FileManager import FileManager
from InputManager import InputManager

from LogManager import LogManager

class CliManager():
    def __init__(self, logManager: LogManager, fileManager: FileManager, inputManager: InputManager) -> None:
        self.logManager = logManager
        self.fileManager = fileManager
        self.inputManager = inputManager
        self.actions = {
            "help": {"function": self.getHelp, "description": "shows functions and descriptions"},
            "get stats": {"function": self.getStats, "description": "get the total statistics about a file"},
            "get percentage": {"function": self.getPercentage, "description": "give the percentage a values appeared in a field"},
            "get counts": {"function": self.getCounts, "description": "give the count of unique values that appeared in a field"},
            "add files": {"function": self.addFiles, "description": "adds files and can take a wildcard ex ./**/*.log"},
            "quit": {"function": self.quit, "description": "exits the program"},
        }

    def addFiles(self):
        value = input("please type the path: ")
        self.fileManager.addFiles(value)

    def start(self):
        shouldContinue = True
        while shouldContinue:
            try:
                selected = self.getSelection(self.actions, "please select action: ")
                result = self.actions[selected]["function"]()
                print(result)
                shouldContinue = result != False
            except ValueError as ex:
                print(f"{type(ex).__name__}: {ex} not found")
            except KeyError as ex:
                print(f"{type(ex).__name__}: {ex} not found")
            except IndexError as ex:
                print(f"{type(ex).__name__}: no values are found")

    def getSelection(self, actions, text="please select: \t"):
        selectedAction = 0
        while True:
            print("\r" + text + ', '.join(
                [action if index != selectedAction else f"[{action}]" for index, action in enumerate(actions)]), end="")
            inputKey = self.inputManager.getKey()
            if inputKey == "right":
                selectedAction += 1
            elif inputKey == "left":
                selectedAction -= 1
            else:
                break

            selectedAction = min(selectedAction, len(actions) - 1)
            selectedAction = max(selectedAction, 0)

        print("\r")
        return list(actions)[selectedAction]

    def getPercentage(self):
        field = self.getSelection(self.logManager.compiledData, "please select field: ")
        value = self.inputManager.input("please type the value that you want: ")

        percentage = self.logManager.getLogPercentage(field, value)

        return f"percentage of {value} is { percentage * 100}%"

    def getCounts(self):
        field = self.getSelection(self.logManager.compiledData, "please select field: ")
        logCounts = self.logManager.getLogCounts(field)
        return f"logs per {field} is {json.dumps(logCounts)}"

    def getStats(self):
        return json.dumps(self.logManager.compiledData, indent= 2)

    def getHelp(self):
        listToPrint = [f"{key}: {value['description']}" for key, value in self.actions.items()]
        return "\n".join(listToPrint) + "\n\nuse left and right arrows to navigate"

    def quit(self):
        return False
