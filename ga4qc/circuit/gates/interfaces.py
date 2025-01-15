from abc import ABC, abstractmethod
from typing import List


class IGate(ABC):

    @abstractmethod
    def __init__(self, qubit_num: int): ...

    @abstractmethod
    def __repr__(self) -> str: ...


class IOptimizableGate(IGate, ABC):

    @property
    @abstractmethod
    def params(self) -> List[float]: ...

    @abstractmethod
    def set_params(self, params: List[float]) -> None: ...
