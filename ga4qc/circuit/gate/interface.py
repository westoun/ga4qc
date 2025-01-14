from abc import ABC, abstractmethod


class IGate(ABC):

    @abstractmethod
    def __init__(self, qubit_num: int): ...
