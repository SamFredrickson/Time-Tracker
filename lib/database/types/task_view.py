from utils.date import get_formatted_difference

class TaskViewType:
    def __init__(self, id, name, start, end, description, date_created) -> None:
        self.__id = id
        self.__name = name
        self.__start = start
        self.__end = end
        self.__description = description
        self.__date_created = date_created

    @property
    def id(self):
        return f'\n[b][white]Number: {self.__id}[/white][/b]'

    @property
    def name(self):
        return f'[b][white]Name: {self.__name}[/white][/b]'

    @property
    def start(self):
        return f'[b][white]Started:[/white] [green]{self.__start}[/green][/b]'
    
    @property
    def end(self):
        if self.__end is None: 
            return f'[b][white]Finished:[/white] [yellow]in progress[/yellow][/b]'
        if self.__end is not None:
            return f'[b][white]Finished:[/white] [green]{self.__end}[/green][/b]'
    
    @property
    def description(self):
        if self.__description is None:
            self.__description = '——'
        return f'[b][grey24]Description: {self.__description}[/grey24][/b]\n'

    @property
    def date_created(self):
        return f'[b][white]Created:[/white] [green]{self.__date_created}[/green][/b]'

    @property
    def total(self):
        total = get_formatted_difference(self.__start, self.__end)
        total = total.replace('(in progress)', '')

        return f'[b][white]Total:[/white] [green]{total}[/green][/b]'

    def get_props(self):
        return [
            self.id,
            self.name,
            self.start,
            self.end,
            self.date_created,
            self.total,
            self.description,
        ]