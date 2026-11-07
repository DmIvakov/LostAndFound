from report import Report

class Manager:
    def __init__(self):
        self.reports: list[Report] = []

    def addReport(self, report):
        self.reports.append(report)

    def removeReport(self, report):
        self.remove(report)

    