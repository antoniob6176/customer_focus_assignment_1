"""
tests LogManager and CliManager using DI and without relying on any environment
"""

from LogManager import LogManager
from CliManager import CliManager


def test1():
    logManager = LogManager()
    logManager.addLog({"action": "a", "result": "success"})
    logManager.addLog({"action": "a", "result": "success"})
    logManager.addLog({"action": "b", "result": "success"})
    logManager.addLog({"action": "b", "result": "success"})
    logManager.addLog({"action": "b", "result": "fail"})

    assert logManager.total == 5, "error in total log count"
    assert logManager.getLogCounts("action")["a"] == 2, "error in log counts"
    assert logManager.getLogPercentage("result", "success") == 0.8, "error in log percentages"


class MockFileManager():
    def addFiles(self, filesPath):
        return True

    def addFile(self, filePath):
        return True

class MockInputManager():
    def __init__(self):
        self.direction = "right"
        self.inputMessage = "a"
        self.count = 0
    def getKey(self):
        oldValue = self.direction
        self.direction = "x"
        return oldValue

    def input(self, _): 
        oldValue = self.inputMessage
        self.inputMessage = "b"
        return oldValue

def test2():
    logManager = LogManager()
    logManager.addLog({"action": "a", "result": "success"})
    logManager.addLog({"action": "a", "result": "success"})
    logManager.addLog({"action": "b", "result": "success"})
    logManager.addLog({"action": "b", "result": "success"})
    logManager.addLog({"action": "b", "result": "fail"})

    fileManager = MockFileManager()

    inputManager = MockInputManager()
    cliManager = CliManager(logManager, fileManager, inputManager)
    counts = cliManager.getCounts()
    percents = cliManager.getPercentage()

    # inputManager would change the input
    cliManager2 = CliManager(logManager, fileManager, inputManager)
    counts2 = cliManager2.getCounts()
    percents2 = cliManager.getPercentage()

    # values need to be different since input is different
    assert counts != counts2, "cli manager didn't switch selection"
    assert percents != percents2, "cli manager didn't switch selection"

def doTests():
    test1()
    test2()
    print("tests succeded")

if __name__ == "__main__":
    doTests()


