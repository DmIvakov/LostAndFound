import json

from src.report import Report

class Manager:
    def __init__(self):
        self._reports: list[Report] = []
        self.loadReports()

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
            json.dump(raw_reports, file, indent=4, sort_keys=True, ensure_ascii=False)
