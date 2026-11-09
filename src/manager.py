import json
from PyQt5.QtCore import QObject, pyqtSignal

from src.report import Report
from src.matcher import Matcher

class Manager(QObject):
    reportsSaved = pyqtSignal()
    reportsLoaded = pyqtSignal()
    reportsMatched = pyqtSignal(str)
    reportsMatchedError = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self._reports: list[Report] = []
        self.loadReports()
        self._filtered: list[Report] = self._reports
        self._active: Report = None
        self._matches: list[Report] = []

    @property
    def reports(self) -> list[Report]:
        return self._reports
    
    @property
    def active(self) -> Report:
        return self._active
    
    @active.setter
    def active(self, value: Report):
        if not isinstance(value, Report):
            raise ValueError("Must be a Report instance!")
        self._active = Report

    @property
    def matches(self) -> list[Report]:
        return self._matches
    
    @matches.setter
    def matches(self, value: list[Report]):
        if not isinstance(value, list):
            raise ValueError("Must be a list!")
            
        if not all(isinstance(item, Report) for item in value):
            raise ValueError("All items in the list must be Report instances!")
            
        self._matches = value

    @property
    def filtered(self) -> list[Report]:
        return self._filtered
    
    @filtered.setter
    def filtered(self, value: list[Report]):
        if not isinstance(value, list):
            raise ValueError("Must be a list!")
            
        if not all(isinstance(item, Report) for item in value):
            raise ValueError("All items in the list must be Report instances!")
            
        self._filtered = value

    def reset(self):
        self._filtered = self._reports
        self._matches = []
        self._active = None

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

    def matchReports(self, reportId) -> int:
        allMatches: dict[int:list[Report]] = Matcher.match(self._reports, self._filtered)

        if reportId in allMatches:
            topMatches = allMatches[reportId]              
            self._active = next((r for r in self._filtered if r.asList[0] == reportId), None) 
            self._matches = topMatches

            for report in topMatches:
                infoStr = f"ID: {", ".join(map(str, report.asList))}"
                self.reportsMatched.emit(infoStr)

        else:
            err = "Brak dopasowań\nspełniających kryteria\n(min. 5 pkt)."
            self.reportsMatchedError.emit(err)
            return 0
        
        return len(topMatches)
    
    def confirmActive(self, reportId) -> bool:
        if self._active != None and reportId >= 0 and reportId < len(self._matches):
            self._active.status = "Rozwiązane"
            self._matches[reportId].status = "Rozwiązane"
            self.saveReports()
            return True
        return False