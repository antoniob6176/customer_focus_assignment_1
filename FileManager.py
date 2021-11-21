import json
from json.decoder import JSONDecodeError
import glob

from LogManager import LogManager


class FileManager():
    def __init__(self, logManager: LogManager) -> None:
        self.logManager = logManager

    def addFiles(self, filesPath):
        try:
            files = glob.glob(filesPath, recursive=True)
            for file in files:
                if self.addFile(file) == True:
                    print(f"file added successfully {file}")
        except FileNotFoundError:
            print(f"file {filesPath} was not found")

    def addFile(self, filePath):  # python doesn't have overloading
        try:
            with open(filePath) as fp:
                for line in fp:
                    log = json.loads(line)
                    self.logManager.addLog(log)
                return True
        except PermissionError as ex:
            print(f"permissons error for: {filePath}")
        except JSONDecodeError as ex:
            print(f"log file not in format: {filePath} {ex}")
        except UnicodeDecodeError as ex:
            print(f"log file not in format: {filePath} {ex}")
