import json

from report import Report

class Manager:
    def __init__(self):
        self._reports: list[Report] = []

    def addReport(self, report):
        self._reports.append(report)

    def removeReport(self, report):
        self._reports.remove(report)

    def clearReports(self):
        self._reports.clear()

    def loadReports(self):
        with open("reports.json", "r", encoding="utf-8") as file:
            self._reports = json.load(file)

    def saveReports(self):
        with open("reports.json", "w", encoding="utf-8") as file:
            json.dump(self._reports, file, indent=4, sort_keys=True, ensure_ascii=False)