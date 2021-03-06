"""
the core of the program stores the data from the logs in a compressed manner 
"""


class LogManager():
    def __init__(self) -> None:
        self.compiledData = {}  # using a dictionary: more simple and json compatible
        self.total = 0

    def addLog(self, jsonObj: dict):
        self.total += 1
        for key, value in jsonObj.items():
            if key not in self.compiledData:
                self.compiledData[key] = {"count": 0, "values": {}}
            if value not in self.compiledData[key]["values"]:
                self.compiledData[key]["values"][value] = 0

            self.compiledData[key]["count"] += 1
            self.compiledData[key]["values"][value] += 1

    def getLogCounts(self, field: str) -> dict:
        return self.compiledData[field]['values']

    def getLogPercentage(self, field: str, value:str) -> float:
        return self.compiledData[field]['values'][value] / self.compiledData[field]['count']
