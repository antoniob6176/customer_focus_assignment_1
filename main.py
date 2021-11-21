"""
program to analise log files, see readme.
"""

import json
import sys
from FileManager import FileManager
from InputManager import InputManager
from LogManager import LogManager
from CliManager import CliManager
import test

if __name__ == "__main__":
    """do the tests then allow to run if succeded"""
    test.doTests()

    args = sys.argv[1:]
    inputManager = InputManager()
    logManager = LogManager()
    fileManager = FileManager(logManager)

    for arg in args:
        fileManager.addFiles(arg)

    # requested stuff from the assignment
    if logManager.total == 0:
        print("no file loaded, skipping assignment answers")
    else: 
        print(f"total number is {logManager.total}")
        print(f"logs per action is {json.dumps(logManager.getLogCounts('action'))}")
        print(f"percentage of success is {logManager.getLogPercentage('result', 'success')}")

    cliManager = CliManager(logManager, fileManager, inputManager)
    cliManager.start()
