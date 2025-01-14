from abc import ABC, abstractmethod

from ga4qc.circuit import Circuit


class IMutation(ABC):
    """Base class of all mutation operations."""

    prob: float = 0.0

    @abstractmethod
    def mutate(self, circuit: Circuit) -> None: ...
