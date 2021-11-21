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
        try:
            with open(filePath) as fp:
                for line in fp:
                    log = json.loads(line)
                    self.logManager.addLog(log)
                return True
        except PermissionError as ex:
            self.outputManager.print(f"permissons error for: {filePath}")
        except JSONDecodeError as ex:
            self.outputManager.print(f"log file not in format: {filePath} {ex}")
        except UnicodeDecodeError as ex:
            self.outputManager.print(f"log file not in format: {filePath} {ex}")
