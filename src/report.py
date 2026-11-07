class Report:
    lastId = 0

    def __init__(self, type, category, color, place, data, status):
        self.id = Report.lastId + 1
        Report.lastId = self.id

        self.type = type
        self.category = category
        self.color = color
        self.place = place
        self.data = data
        self.status = status

    
