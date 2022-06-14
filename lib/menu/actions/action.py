from abc import abstractmethod


class Action:
    '''This class defines logic of items in menu.'''
    @abstractmethod
    def do(cls):
        pass
        