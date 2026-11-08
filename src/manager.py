import json
from PyQt5.QtCore import QObject, pyqtSignal

from src.report import Report
from src.matcher import Matcher

class Manager(QObject):
    reportsSaved = pyqtSignal()
    reportsLoaded = pyqtSignal()

    def __init__(self):
        super().__init__()
        self._reports: list[Report] = []
        self._filtered: list[Report] = []
        self.loadReports()

    @property
    def reports(self) -> list[Report]:
        return self._reports

    @property
    def filtered(self) -> list[Report]:
        return self._filtered
    
    @filtered.setter
    def filtered(self, value: list[Report]):
        if not isinstance(value, list):
            raise ValueError("Must be a list!")
            
        if not all(isinstance(item, Report) for item in value):
            raise ValueError("All items in the list must be Report instances!")
            
        self._reports = value

    def clearFiltered(self):
        return self._filtered.clear()

    # def getReportsCount(self) -> int:
    #     return len(self._reports)

    def createReport(self, **fields) -> Report:
        return Report(**fields)

    def addReport(self, report):
        self._reports.append(report)
        self.saveReports()

    def createAndAddReport(self, **fields) -> Report:
        report = self.createReport(**fields)
        self.addReport(report)
        return report

    def removeReport(self, report):
        self._reports.remove(report)
        self.saveReports()

    def clearReports(self):
        self._reports.clear()
        self.saveReports()

    def loadReports(self):
        try:
            with open("reports.json", "r", encoding="utf-8") as file:
                data = json.load(file)

                self._reports = [self.createReport(**item) for item in data]
                
                if self._reports:
                    Report.lastId = max(r.id for r in self._reports)

            self.reportsLoaded.emit()
                    
        except (FileNotFoundError, json.JSONDecodeError):
            self._reports = []

    def saveReports(self):
        with open("reports.json", "w", encoding="utf-8") as file:
            raw_reports = [
                {
                    "id": report.id,
                    "status": report.status,
                    "type": report.type,
                    "category": report.category,
                    "color": report.color,
                    "place": report.place,
                    "date": report.date
                }
                for report in self._reports
            ]
            raw_reports.sort(key=lambda x: x["id"])
            json.dump(raw_reports, file, indent=4, sort_keys=False, ensure_ascii=False)

        self.reportsSaved.emit()
