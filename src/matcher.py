from src.report import Report

class Matcher:
    @classmethod
    def getCleanText(text) -> str:
        return text.strip().lower()
    
    @classmethod
    def calculatePoints(cls, report1, report2) -> int:
        points = 0

        print(report1.asList[2:5])
        print(report2.asList[2:5])
