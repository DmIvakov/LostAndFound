class Report:
    lastId = 0

    def __init__(self, type, category, color, place, date, id=None, status="Zgubiono"):
        if id is not None:
            self.__id = id
        else:
            Report.lastId += 1
            self.__id = Report.lastId

        self.__status = status
        
        self.type = type
        self.category = category
        self.color = color
        self.place = place
        self.date = date


    # --- ID ---
    @property
    def id(self) -> int:
        return self.__id

    # --- STATUS ---
    @property
    def status(self) -> str:
        return self.__status

    @status.setter
    def status(self, value: str):
        if value not in ["Zgubiono", "Znaleziono", "Rozwiazane"]:
            raise ValueError("Status must be 'Zgubiono', 'Znaleziono' or 'Rozwiazane'")
        self.__status = value

    # --- TYPE ---
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, value: str):
        self.__type = value

    # --- CATEGORY ---
    @property
    def category(self) -> str:
        return self.__category

    @category.setter
    def category(self, value: str):
        self.__category = value

    # --- COLOR ---
    @property
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self, value: str):
        self.__color = value

    # --- PLACE ---
    @property
    def place(self) -> str:
        return self.__place

    @place.setter
    def place(self, value: str):
        self.__place = value

    # --- date ---
    @property
    def date(self) -> str:
        return self.__date

    @date.setter
    def date(self, value: str):
        self.__date = value
