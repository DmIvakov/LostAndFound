from datetime import datetime

from src.report import Report

class Matcher:
    @staticmethod
    def getCleanText(text) -> str:
        if text is None:
            return ""
        return " ".join(str(text).lower().split())
    
    @classmethod
    def calculatePoints(cls, report1, report2) -> int:
        # using list of Report's intstance fields
        # we're looking for the fields from 2 to 5 (inclusive)
        ###############################
        # index |   field    | points #
        # ------|------------|------- #
        #   2   | 'category' |   3    #
        #   3   |  'color'   |   2    #
        #   4   |  'place'   |   1    #
        #   5   |  'date'    |   2    #
        ###############################
        # dates match if diff(date1, date1) <= 7 days
     
        scoringMap = {2: 3, 3: 2, 4: 1}
        points = 0

        r1List = report1.asList
        r2List = report2.asList

        for i in range(2, 5): 
            if cls.getCleanText(r1List[i]) == cls.getCleanText(r2List[i]):
                points += scoringMap[i]

        try:
            date1 = datetime.strptime(str(r1List[5]).strip(), "%d.%m.%Y")
            date2 = datetime.strptime(str(r2List[5]).strip(), "%d.%m.%Y")
            delta_days = abs((date1 - date2).days)
            if delta_days <= 7:
                points += 2
        except (ValueError, TypeError):
            pass  
    
        return points

    @classmethod
    def match(cls, reports, filtered) -> dict:
        allMatches = {}

        for currentReport in filtered:
            matchedResults = []
            
            currentId = currentReport.asList[0]
            currentType = cls.getCleanText(currentReport.asList[1])
            currentCategory = cls.getCleanText(currentReport.asList[2])

            for report in reports:
                rList = report.asList
                
                if rList[0] == currentId:
                    continue

                if cls.getCleanText(rList[6]) != "otwarte":
                    continue

                if cls.getCleanText(rList[1]) == currentType:
                    continue

                if cls.getCleanText(rList[2]) != currentCategory:
                    continue

                points = cls.calculatePoints(currentReport, report)

                if points >= 5:
                    matchedResults.append((points, report))

            matchedResults.sort(key=lambda x: x[0], reverse=True)

            topThree = [report for points, report in matchedResults[:3]]
            
            if topThree:
                allMatches[currentId] = topThree

        return allMatches