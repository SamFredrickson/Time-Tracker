class DateRange:
    def __init__(self, date_from: str, date_to: str) -> None:
        self.__date_from = date_from
        self.__date_to = date_to

    @property
    def date_from(self):
        return self.__date_from

    @property
    def date_to(self):
        return self.__date_to

    @property
    def date_range_formatted(self):
        '''Get date range format (from-to) if from != to'''
        if self.__date_from == self.__date_to:
            return self.__date_from
        return f'{self.__date_from}-{self.__date_to}'