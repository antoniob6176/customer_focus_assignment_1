"""
handles parsing the files and sending the data to the log manager
"""

import json
from json.decoder import JSONDecodeError
import glob

from LogManager import LogManager
from OutputManager import OutputManager


class FileManager():
    def __init__(self, logManager: LogManager, outputManager: OutputManager) -> None:
        self.logManager = logManager
        self.outputManager = outputManager

    def addFiles(self, filesPath):
        """adds files and can take a wildward pattern ex ./input/log*.log"""
        try:
            files = glob.glob(filesPath, recursive=True)
            if not files:
                self.outputManager.print(f"couldn't find files for: {filesPath}")
            for file in files:
                if self.addFile(file) == True:
                    self.outputManager.print(f"file added successfully {file}")
        except FileNotFoundError:
            self.outputManager.print(f"file {filesPath} was not found")

    def addFile(self, filePath):
        """adds the log file to the log manager, stops on first error"""
        try:
            with open(filePath) as fp:
                for line in fp: 
                    # we can add more log fomats here ex: CSV
                    log = json.loads(line) # this format is one JSON per line
                    self.logManager.addLog(log)
                return True
        except PermissionError as ex:
            self.outputManager.print(f"permissons error for: {filePath}")
        except JSONDecodeError as ex:
            self.outputManager.print(f"log file not in correct format: {filePath} {ex}")
        except UnicodeDecodeError as ex:
            self.outputManager.print(f"log file not in correct format: {filePath} {ex}")
        except IsADirectoryError:
            self.outputManager.print(f"this is a directory: {filePath}")

