"""
program to analise log files, please see readme.
"""

import json
import sys
from FileManager import FileManager
from InputManager import InputManager
from OutputManager import OutputManager
from LogManager import LogManager
from CliManager import CliManager


if __name__ == "__main__":
    args = sys.argv[1:]
    inputManager = InputManager()
    outputManager = OutputManager()
    logManager = LogManager()
    fileManager = FileManager(logManager, outputManager)

    for arg in args:
        fileManager.addFiles(arg)

    # requested stuff from the assignment
    if logManager.total == 0:
        print("no file loaded, skipping assignment answers")
    else: 
        print(f"total number is {logManager.total}")
        print(f"logs per action is {json.dumps(logManager.getLogCounts('action'))}")
        print(f"percentage of success is {int(logManager.getLogPercentage('result', 'success') * 100)}")
        print("")
    cliManager = CliManager(logManager, fileManager, inputManager, outputManager)
    cliManager.start()
